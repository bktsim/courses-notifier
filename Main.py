from Course import Course
from discord_webhook import DiscordWebhook
import time

DISCORD_ID = "aaa"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/828988872637153350/fzvm-Miepyd5G3GTmgjpz1Wzm45600AiEUSZ7QfwBL1H9jUac9wgMPQZqRrTyBN051HJ"

COURSES = [
    Course("COMM 293 922", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=COMM&course=293&section=922", True),
    Course("WRDS 150B 511", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=511", False),
    Course("WRDS 150B 512", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=512", False),
    Course("WRDS 150B 513", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=513", False),
    Course("WRDS 150B 520", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=520", False),
    Course("WRDS 150B 521", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=521", False),
    Course("WRDS 150B 522", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=522", False),
    Course("WRDS 150B 523", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=523", False),
    Course("WRDS 150B 551", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=551", False),
    Course("WRDS 150B 552", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=552", False),
    Course("WRDS 150B 561", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=561", False),
    Course("WRDS 150B 562", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=562", False),
    Course("WRDS 150B 563", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=563", False),
    Course("WRDS 150B 564", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=564", False),
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
