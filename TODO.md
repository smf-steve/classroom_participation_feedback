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

  1. Determine if we need to delay the immediate publication on feedback
     - so far no issues, but what if something "inappropriate" is posted.

### Features
  1. Add the ability to add emojis for feedback, like party parrot
  
### Bugs
  1. Should the 2:00 class appear before or after the 9:00 class... (i.e. sort by military time)
  1. Heading Values (e.g., Prompt) should be bolded to allow them to stand out more

  1. The Class Description should be placed into readonly textarea... ?
     Ditto for the feedback
     This will unify the way it looks?
  1. in dark mode, the slide range is not apparent
     - should the slide provide the value selected. 
  1. index.cgi : individual class information
     - Default inputs should be provided in the Class Description
     - but when said information is provide, that saved information should be presented
     - consider put the prompt above the QR code.

  1. index.cgi
     - if you submit with nothing, then the placeholder inforamtion is wipped out.
        - either
         1. the placeholder information should be used,
         1. the defaults should be placed back int.
  1. input.cgi
     - the font in the placeholder should be such that it is know that it is readonly
       i.e., already provided.

  1. after the submit, it should got to the index.cgi page, but at the href of today's info.

   

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




