/*
  A class that represents a course
  
  String courseName: name of course
  String link: URL to course registration page
  Dict sections: {"course-code": trackRestrictedSeats}, where course-code is the 3/4 digit/alphabet identifier, and trackRestrictedSeats determines whether restricted seats are tracked
  
  Constructor: new Course(courseName, link, {"course-code": trackRestrictedSeats ...})
*/
class Course {

  constructor(name, link, sections) {
    this.courseName = name;
    this.link = link;
    this.sections = sections;
  }

  checkSeats() {
    const content = UrlFetchApp.fetch(this.link).getContentText();
    const $ = Cheerio.load(content);
    
    const rows = $('table.table-striped.section-summary tbody').find("tr");
    var checked = {}; // Ensure that it is only checked once

    for (var i = 0; i < rows.length; i++) {
      var current = rows[i];
      var td = $(current).children("td");
      var seats = $(td[0]).text().trim();
      var section = $(td[1]).children("a");
      var sectionUrl = $(section).attr("href");
      section = $(section).text().replace(this.courseName, "").trim();
      
      if (this.sections[section] != null && checked[section] == null) {
        if ((seats == "Restricted" && this.sections[section]) || seats == "") {
          Logger.log(this.courseName + " " + section + " | SEAT FOUND");
          sendNotification(this.courseName + " " + section, this.link + sectionUrl);
        } else { // Blocked or Full
          Logger.log(this.courseName + " " + section + " | SEATS NOT FOUND");
        }

        checked[section] = "";
      }
    }
  }
};

// ==================================================================================================================================================================
/*
  CONFIGURATION
    - Change discordId to your Discord ID
    - Change discordWebhook to your Discord Webhook URL
    
  courses is an array of courses to iterate (check) through. A course is left as an example in the array.  
    - Add courses that you want to get seats into the courses array
*/
const discordId = ""
const discordWebhook = "";
const discordTag = "<@" + discordId + ">";

const courses = [
  new Course("CPSC 121", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=CPSC&course=121",
    {"201": true, "L1A": false}
  ),
];
// ==================================================================================================================================================================

/*
  Runs the script to check courses.
*/
function findCourses() {
  for (var i = 0; i < courses.length; i++) {
    courses[i].checkSeats();
  }
}

/*
  Course course: The course with seats available
  CITATION: https://www.labnol.org/code/20563-post-message-to-discord-webhooks
  
  Sends a message to the discord webhook if a course is found to have empty seats.
*/
function sendNotification(courseName, sectionUrl) {
  var message = discordTag + ", there is a seat opening for " + courseName + " @ " + sectionUrl;

  var params = {
    headers: {
      'Content-Type': 'application/json'
    },
    method: "POST",
    payload: JSON.stringify({content: discordTag, embeds: [
      {
        "title": courseName,
        "description":  "**Seat Available:** **__[Click here!]__**(" + sectionUrl + ")"
      }
    ]}),
    muteHttpExceptions: true
  };

  var response = UrlFetchApp.fetch(discordWebhook, params);
}
