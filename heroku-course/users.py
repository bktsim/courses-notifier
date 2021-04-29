from models import *

users = [
    {
        "user": User("discord_id_1", "discord_webhook_url_1"),
        "courses": [
            {
                "course": RegisterCourse("STAT 251", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=STAT&course=251"),
                "sections": [RegisterSection("921", False)],
            },
            {
                "course": RegisterCourse("CPSC 221", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=CPSC&course=221"),
                "sections": [RegisterSection("911", False)],
            },
        ]
    },
    {
        "user": User("discord_id_2", "discord_webhook_url_2"),
        "courses": [
            {
                "course": RegisterCourse("COMM 293", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=COMM&course=293"),
                "sections": [RegisterSection("922", True)],
            },
            {
                "course": RegisterCourse("WRDS 150B", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=WRDS&course=150B"),
                "sections": [RegisterSection("511", False), RegisterSection("512", False), RegisterSection("513", False),
                             RegisterSection("520", False), RegisterSection("521", False), RegisterSection("522", False),
                             RegisterSection("523", False), RegisterSection("551", False), RegisterSection("552", False),
                             RegisterSection("561", False), RegisterSection("562", False), RegisterSection("563", False),
                             RegisterSection("564", False)],
            },
        ]
    },
]


