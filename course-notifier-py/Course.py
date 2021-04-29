import requests
from bs4 import BeautifulSoup
import re

class Course:
    def __init__(self, courseName, courseURL, checkForRestrictedSeats):
        """
            (String) courseName: name of the course
            (String) courseURL: URL to the section of the course
            (Boolean) checkForRestrictedSeats: whether or not to check for restricted seats
        """
        self.courseName = courseName
        self.courseURL = courseURL
        self.checkForRestrictedSeats = checkForRestrictedSeats

    # getters
    def getCourseName(self):
        return self.courseName
    
    def getCourseURL(self):
        return self.courseURL
    
    def getCheckForRestrictedSeats(self):
        return self.checkForRestrictedSeats

    # sends GET to coruseURL. 
    # return True if seats are available, False otherwise.
    def checkForSeats(self):
        soup = BeautifulSoup(requests.get(self.courseURL).content, "html.parser")
        generalSeats = int(re.search("\d+", str(soup.select("tr:nth-child(4) strong")[0])).group(0))
        restrictedSeats = int(re.search("\d+", str(soup.select("tr:nth-child(5) strong")[0])).group(0))
        
        if (generalSeats > 0) or (self.checkForRestrictedSeats and restrictedSeats > 0):
            return True
        else:
            return False