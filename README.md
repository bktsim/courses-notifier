# courses-gs
course-notifier but written in google scripts.

## Usage
1. Edit the courses array and create courses that you want to track.
  * For example: `new Course("WRDS 150B 511", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=511", false)`
    to track this specific WRDS course. The third argument (true, false) should be edited depending on whether or not you have access to restricted seats.
2. Create a Discord Webhook and put the URL (as a string) into `const discordWebhook` as a string.
3. Find your Discord ID (right click your profile and copy ID) and put it into `const discordID` as a string.
4. Copy the code and paste it in a new Google Apps Script
5. Install Cheerio in Libraries (Script ID: 1ReeQ6WO8kKNxoaA_O0XEQ589cIrRvEBA9qcWpNqdOP17i47u6N9M5Xh0)
6. Create a time-based trigger that runs every minute.
