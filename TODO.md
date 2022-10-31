### Things to do
  1. Restructure the filesystem for proper placement of public and nonpublic files

  1. Update the main page to allow the faculty member to record
     - what was dicussed in class
     - the prompt
     - the number of students attended
  1. Determine what other types of re-encoding needs to be performed on student responses
     - For example:
       * Student feedback: lots of info provided%2C need to review to understand completely
       * Published feedback: lots of info provided, need to review to understand completely
       * See: https://www.tutorialspoint.com/html/html_url_encoding.htm
  1. Style, Style, Style
  1. Update not-in-session.png -- missing minor square
  1. Determine why the CGI process is support slow on www.csun.edu -- solved!
  1. Determine if we need to delay the immediate publication on feedback
     - so far no issues, but what if something "inappropriate" is posted.

### Features
  1. Add a summary field by the faculty member indicate what was dicussed in class.
     - this could be the Prompt.
  1. Consider adding a graph showing the associated modes from the scale marks
  1. Add the ability to add emojis for feedback, like party parrot
  
### Bugs
  1. List of ratings can overflow the div.
     - can this be turned into a tool tip 
     - perhaps, it can be <div>Range: 3 4 ... 7 8</div>
       - just showing the two lowest and the two highest
       - then use a tool tip to allow the user to see them all
       - perhaps a graph would be better or make this range obsolete 

### Refactor
  1. rewrite the protoype in an appropriate MVC web langauge
  1. Create a QR code on the fly with an embedded code 
     1. to limit spruious usage of the system
     1. to encode class session information (reduce the number of fields to post)

### Presentation
  1. Put a repo link on the index.html page

### Exploration
  1. Determine if an .htaccess file can
     1. allow users to authenticate with their @my.csun.edu address
        1. ensure that their authentication can be cached
  1. Consider a login button to allow the faculty member 
     1. to modify a prompt on the fly
     1. to record number of students in attendence.
  1. Determine if the registered number of students should be presented on the page
     - then the number of attendees have some mean as to 70% - 80%, etc.




