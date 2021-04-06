const discordId = ""
const discordTag = "<@" + discordId + ">";
const discordWebhook = "";

const appCooldown = 10000; // in milliseconds

/*
  String courseName: name of course
  String link: URL to course registration page
  Boolean trackRestrictedSeats: true if user is eligible for restricted seats for that specific section
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

// example course left (as example)
const courses = [
  new Course("WRDS 150B 511", "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=WRDS&course=150B&section=511", false),
];

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
  String courseName: Name of the course
  https://www.labnol.org/code/20563-post-message-to-discord-webhooks
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
*/
function getSeats(link) {
  const content = UrlFetchApp.fetch(link).getContentText();
  const cheerio = Cheerio.load(content);
  
  var generalSeats = cheerio('tr:nth-child(3) strong').text();
  var restrictedSeats = cheerio('tr:nth-child(4) strong').text();

  return [Number(generalSeats), Number(restrictedSeats)];
}

