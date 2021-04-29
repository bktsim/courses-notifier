import time
from users import *

courses: list[Course]
courses = []

COOLDOWN = 5


def main():
    initUsers()
    print("=======\nSetup complete\n\n\n\n")
    while True:
        for course in courses:
            course.checkCourseSeats()
        time.sleep(COOLDOWN)


def initUsers():
    for user in users:
        for course_data in user["courses"]:
            course = course_data["course"]
            sections = course_data["sections"]

            course.setUser(user["user"])

            for section in sections:
                course.addSection(section)
                section.setCourse(course)

            registerCourse(user["user"], course)


def registerCourse(user: User, user_course: RegisterCourse) -> None:
    registered = False

    for course in courses:
        if course.getName() == user_course.getName():
            print("REGISTER: Registering user " + user.getDiscordId() + " into course " + course.getName())
            registerSections(user, course, user_course.getSections())
            registered = True

    if not registered:
        course = Course(user_course.getName(), user_course.getUrl())
        print("CREATE: Creating course " + course.getName())
        courses.append(course)
        print("REGISTER: Registering user " + user.getDiscordId() + " into course " + course.getName())
        registerSections(user, course, user_course.getSections())


def registerSections(user: User, course: Course, user_course_sections: list[RegisterSection]) -> None:
    for register_section in user_course_sections:
        course.getSection(register_section.getName()).addUser(user, register_section.getRestricted())


if __name__ == '__main__':
    main()

