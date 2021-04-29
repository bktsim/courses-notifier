# courses-notifier

This application is capable of tracking restricted and general seats for UBC classes. The file with `.gs` extension is a script that can be used on Google Apps Script. The file(s) with `.py` extension is a script that can be used locally on a computer. The folder and files inside `heroku-course` is a version that can be deployed onto Heroku and ran on a Dyno. It is the most sophisticated version and contains the use of OOP and the observer pattern.

The application checks for available seats every n seconds, and pings the user by sending a message via a Discord webhook into a private channel if a seat is available.

**Note:** This project is not intended for actual use - it is just a fun project I decided to create during my free time. 

### Usage
You need the following libraries to run the python files:
 * discord_webhook
 * BeautifulSoup4
 * requests

You need the following libraries to run the Google Apps Script file:
* Cheerio
