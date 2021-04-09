from Course import Course
from discord_webhook import DiscordWebhook
import time

DISCORD_ID = ""
DISCORD_WEBHOOK = ""

COURSES = [
    Course("COMM 293 922", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=COMM&course=293&section=922", True),
]

def Main():
    while True:
        for course in COURSES:
            if Course.checkForSeats(course):
                print("SEATS FOUND FOR " + course.getCourseName())
                sendWebhook(course)
                time.sleep(2)
            else:
                print("NO SEATS FOUND FOR " + course.getCourseName())
        time.sleep(10)

def sendWebhook(course):
    discordTag = "<@" + DISCORD_ID + ">"
    DiscordWebhook(url=DISCORD_WEBHOOK, content=discordTag + ", a seat is available for " + course.getCourseName() + " at " + course.getCourseURL()).execute()

Main()
