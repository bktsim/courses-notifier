from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup
import requests


class RegisterUser:
    """
    Represents a user (observer)
    User user: User to notify
    bool restricted: Whether the user is eligible for restricted seats.
    """

    def __init__(self, user, restricted: bool):
        self.__user = user
        self.__restricted = restricted

    def __eq__(self, other) -> bool:
        return isinstance(other, RegisterUser) and \
               self.__user.getDiscordId() == other.getUser().getDiscordId()

    def getUser(self):
        return self.__user

    def getRestricted(self) -> bool:
        return self.__restricted


class RegisterSection:
    """
    Represents a section that a user may want to register in.
    RegisterCourse course: The course that the user is trying to register in.
    str name: Name of the section
    bool restricted: Whether the user is eligible for restricted seats.
    """

    def __init__(self, name: str, restricted: bool):
        self.__course = None
        self.__name = name
        self.__restricted = restricted

    def setCourse(self, course):
        self.__course = course

    def getCourse(self):
        return self.__course

    def getName(self) -> str:
        return self.__name

    def getRestricted(self) -> bool:
        return self.__restricted


class RegisterCourse:
    """
    Represents the courses that a user may want to register in.
    User user: User that is trying to register in the course
    str name: Name of the course
    str url: Url to the general course page
    list[RegisterSection]: List of sections that the user is interested in registering for.
    """

    def __init__(self, name: str, url: str):
        self.__name = name
        self.__user = None
        self.__url = url
        self.__sections = []

    def addSection(self, section: RegisterSection):
        if section not in self.__sections:
            self.__sections.append(section)

    def setUser(self, user):
        self.__user = user

    def __eq__(self, other) -> bool:
        return (isinstance(other, RegisterCourse) and
                (self.getName() == other.getName() and self.getUser() == other.getUser())) or \
               (isinstance(other, Course) and (self.getName() == other.getName()))

    def getName(self) -> str:
        return self.__name

    def getUser(self) -> str:
        return self.__user

    def getUrl(self) -> str:
        return self.__url

    def getSections(self) -> list[RegisterSection]:
        return self.__sections


class User:
    """
    Represents a user of the application.
    str discord_id: ID for their discord tag.
    str discord_webhook: URL for their discord webhook.
    list[RegisterCourse]: A list of courses that they are interested in.
    """

    def __init__(self, discord_id: str, discord_webhook: str):
        self.__discord_id = discord_id
        self.__discord_webhook = discord_webhook
        self.__courses = []

    def addCourse(self, course: RegisterCourse) -> None:
        if course not in self.__courses:
            self.__courses.append(course)

    def getDiscordId(self) -> str:
        return self.__discord_id

    def getDiscordWebhook(self) -> str:
        return self.__discord_webhook

    def notify(self, section) -> None:
        DiscordWebhook(
            url=self.__discord_webhook,
            content="<@" + self.__discord_id + ">, There is a seat available for " +
                    section.getCourse().getName() + " " + section.getName() + "!" + "\n" + section.getUrl()).execute()


class Section:
    """
    Represents a section of a course.
    str name: Name of the section (e.g. 902 or L1A)
    str url: Url to the section registration link.
    Course course: The course that the section is under
    list[RegisterUser] users: Users that are listening to this section for updates.
    """

    def __init__(self, name: str, url: str, course):
        self.__name = name
        self.__url = url
        self.__course = course
        self.__users = []

    def __eq__(self, other) -> bool:
        return isinstance(other, Section) and other.getName() == self.__name

    def getName(self) -> str:
        return self.__name

    def getUrl(self) -> str:
        return self.__url

    def getCourse(self):
        return self.__course

    def addUser(self, user: User, restricted: bool) -> None:
        userToAdd = RegisterUser(user, restricted)
        if userToAdd not in self.__users:
            print("ADD: "
                  "Adding user " + user.getDiscordId() + " to course " + self.__course.getName() + " " + self.__name)
            self.__users.append(userToAdd)

    def notifyUsers(self, restricted_only: bool) -> None:
        if len(self.__users) == 0:
            return None

        print(("RESTRICTED " if restricted_only else "SEAT FOUND FOR: ") + self.__course.getName() + " " + self.__name)

        for register_user in self.__users:
            if (not restricted_only) or (restricted_only and register_user.getRestricted()):
                print("Notifying " + register_user.getUser().getDiscordId() + " for " +
                      self.__course.getName() + " " + self.__name)
                register_user.getUser().notify(self)


class Course:
    """
    Represents a course.
    str name: Name of the course
    str url: Link to the course url.
    dict[Section] sections: Sections that the course has.
    """

    def __init__(self, name: str, url: str):
        self.__name = name
        self.__url = url
        self.__sections = {}
        self.__setup()

    def __eq__(self, other) -> bool:
        return isinstance(other, Course) and other.__name == self.__name

    def getName(self) -> str:
        return self.__name

    def getUrl(self) -> str:
        return self.__url

    def getSection(self, name: str) -> Section:
        for section_name in self.__sections:
            if section_name == name:
                return self.__sections[section_name]
        raise Exception("ERROR: The specified section " + name + " was not found in the course " + self.__name)

    def __setup(self):
        return self.checkCourseSeats()

    # Sets up course by adding all sections if the self.__sections is empty.
    # Otherwise, fetch data from course_url and notify users if any seats are available.
    def checkCourseSeats(self):
        soup = BeautifulSoup(requests.get(self.getUrl(), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}).content, "html.parser").select(".section-summary")[0]
        setup = True if len(self.__sections) == 0 else False

        for section in soup.select(".section1, .section2"):
            results = section.find_all("td")
            link = results[1].find("a")

            # prevent weird courses
            if link:
                section_name = link.contents[0].replace(self.getName(), "").strip()
                url = "https://courses.students.ubc.ca" + link['href']

                general_seats = True if len(results[0].contents[0].strip()) == 0 else False
                restricted_seats = True if results[0].contents[0] == "Restricted" else False

                if setup:
                    # No users, so no need to notify.
                    self.__sections[section_name] = Section(section_name, url, self)
                else:
                    if self.__sections[section_name] is None:
                        raise Exception("ERROR: Problem in setup. Section not found!")
                    else:
                        # If any seats are available (general or restricted)
                        if general_seats or restricted_seats:
                            self.__sections[section_name].notifyUsers(False if general_seats else restricted_seats)

        print("Checking complete for " + self.__name)
