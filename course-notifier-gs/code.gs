/*
  A class that represents a course
  
  String courseName: name of course
  String link: URL to course registration page
  Boolean trackRestrictedSeats: true if user is eligible for restricted seats for that specific section
  
  Constructor: new Course(courseName, link, trackRestrictedSeats)
*/
class Course {

  constructor(name, link, trackRestrictedSeats) {
    this.courseName = name;
    this.link = link;
    this.trackRestrictedSeats = trackRestrictedSeats;
  }

  hasSeats() {
    var results = getSeats(this.link);
    if ((this.trackRestrictedSeats && results[1] > 0) || (results[0] > 0)) {
      return true;
    }
    return false;
  }

  getCourseName() {
    return this.courseName;
  }

  getCourseURL() {
    return this.link;
  }
};

/*
  CONFIGURATION
    - Change discordId to your Discord ID
    - Change discordWebhook to your Discord Webhook URL
    - ONLY increase appCooldown - do NOT decrease appCooldown - you will get in trouble.
    
  courses is an array of courses to iterate (check) through. A course is left as an example in the array.  
    - Add courses that you want to get seats into the courses array
*/
const discordId = ""
const discordWebhook = "";
const appCooldown = 10000; // in milliseconds
const courses = [
  new Course("WRDS 150B 511", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=511", false),
];
const discordTag = "<@" + discordId + ">";

/*
  Runs the script to check courses - and terminates it after a minute to prevent overlapping with the next trigger.
*/
function findCourses() {
  var startTime = Date.now();
  while (Date.now() - startTime < 60000) {
    for (var i = 0; i < courses.length; i++) {
      var c = courses[i]
      if (c.hasSeats()) {
        sendNotification(c);
        Logger.log("SEATS FOUND FOR " + c.getCourseName());
        Utilities.sleep(2000);
      } else {
        Logger.log("NO SEATS FOUND FOR " + c.getCourseName());
      }
    }
    Utilities.sleep(appCooldown);
  }
}

/*
  Course course: The course with seats available
  CITATION: https://www.labnol.org/code/20563-post-message-to-discord-webhooks
  
  Sends a message to the discord webhook if a course is found to have empty seats.
*/
function sendNotification(course) {
  var message = discordTag + ", there is a seat opening for " + course.getCourseName() + " at " + course.getCourseURL();

  var params = {
    headers: {
      'Content-Type': 'application/json'
    },
    method: "POST",
    payload: JSON.stringify({content: message}),
    muteHttpExceptions: true
  };

  var response = UrlFetchApp.fetch(discordWebhook, params);
}

/*
  String link: URL to course registration page
  
  Sends a request to the ssc link and checks the number of general and restricted seats available for that course.
*/
function getSeats(link) {
  const content = UrlFetchApp.fetch(link).getContentText();
  const cheerio = Cheerio.load(content);
  
  var generalSeats = cheerio('tr:nth-child(3) strong').text();
  var restrictedSeats = cheerio('tr:nth-child(4) strong').text();

  return [Number(generalSeats), Number(restrictedSeats)];
}