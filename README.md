# courses-gs
[course-notifier](https://github.com/bktsim/course-notifier), but it's written for use in Google App Scripts.
Please note that this is not intended for actual use - it is just a fun project that I decided to write during my free time. I take no liability/responsibility for any consequences that occur from using this application. 

## Usage
1. Edit the courses array and create courses based on the courses that you want to track.
  * The course class has parameters `String courseName, String URL, Boolean trackRestrictedSeats`.
  * For example: `new Course("WRDS 150B 511", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=511", false)` means that you are tracking WRDS 150B 511, the link to the course is that, and that you have no access to restricted seats.
  * Add as many as you want (add commas to the end for multiple entries)
2. Create a Discord Webhook and put the URL (as a string) into `const discordWebhook` as a string.
3. Find your Discord ID (right click your profile and copy ID) and put it into `const discordID` as a string.
4. Copy the code and paste it in a new Google Apps Script
5. Install Cheerio in Libraries (Script ID: 1ReeQ6WO8kKNxoaA_O0XEQ589cIrRvEBA9qcWpNqdOP17i47u6N9M5Xh0)
6. Create a time-based trigger that runs every minute.
