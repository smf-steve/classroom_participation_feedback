# Classroom Participation, Response, and Feedback System

A simple system to allow students to provided key information about a class meeting.  

After a lecture, many instructors are interested in obtaining feedback from their students.  This feedback could be related to the material presented, to how the material was presented, or to how well the student's understood the material presented.

A survey can be given at the end of class to obtain information from the students. To be effective, this survey must be quick and easy to complete: a simple rating (0..10) of the class and the opportunity to provide free-form feedback.  The focus of the feedback can also be increased by allowing the Professor to provide a prompt to guide the student's feedback respons.  (Note that such a survey should never devolve into an end-of-class quiz.)


### Classroom Workflow
  1. Instructor projects a QR code on the screen
  1. Students take a picture of a QR code
     - said QR code is only valid during a finite time-window
  1. Students fill out a web form with the following information
     - email address / github account / a personal identifier
     - rating of the class (low=0 .. high=10)
     - text response (possible to a specific prompt)

#### Possible Upgrades:
  * Student Authentication 
    - to allow caching of email address
    - to limit feedback to just register students

#### Status: 
  * A prototype system, built quickly, using CGI using the bash shell.

#### Gaming the System

The system is designed to allow students who attended the class to provide feedback.  If the feedback collected is used as part of the grading system, student's who don't attend class might feel pressured to game the system.  

Tighter controls could be placed on the process to collect feedback.  Student's who don't attend may continue to find ways to circumvent each new control.  Such controls can also have a negative impact on student's who attend class because now their candid feedback is being used as part of the grading process.

In short, we specifically designed the system with a reduce set of controls.  Sure we might received some bogus feedback, but we believe such feedback will equate to some noise in the data.

---
### Pages
1. Master page (Faculty Access Only)
   * URL:  participation/index.cgi
   * Purpose: Provide a QR code for students to access the system
   * Specification:
     - page only accessable by faculty member
     - QR code faculty member projects the page on the board
       *

1. Feedback input Page
   * URL: 
   * Purpose: Gather information from student
   * Specification:

1. Logger
   * Purpose: Log the information provided by students