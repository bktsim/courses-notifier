# courses-notifier

This application is capable of tracking restricted and general seats for UBC classes. 
The application checks for available seats every n seconds, and pings the user by sending a message via a Discord webhook into a private channel if a seat is available.

* The application in `course-notifier-gs` with the `.gs` extension is a script that can be deployed on Google Apps Script and used with Triggers.
* The application in `course-notifier-py` can be used locally on a computer. 
* The application in `heroku-course` is based on python, and can be deployed on the Heroku platform with a Free Dyno. It is the most "sophisticated" version based on OOP and the observer pattern. Much more scalable for multiple users. It is also more "smart" and checks for seat availability in a smarter way.

**Note:** This project is not intended for actual use - it is just a fun project I decided to create during my free time. 

### Usage
You need the following libraries to run the python files:
 * discord_webhook
 * BeautifulSoup4
 * requests

You need the following libraries to run the Google Apps Script file:
* Cheerio
