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
  1. Add the ability to add emojis for feedback, like party parrot


  1. Determine if we need to delay the immediate publication on feedback
     - so far no issues, but what if something "inappropriate" is posted.

  1. Update the init_report.cgi to require authentication

### Presentation and CSS 
  1. Put a repo link on the index.html page
  1. fix rendering boxes for bottom of page (index.cgi)

  1. move css to a file

  1. put in href for current class?
     -  <p id=news>
     -  <a href="#news">Go</a>
  1. modify the text of the placeholder

  1. modify the text of the Class Coverage placeholder to render not as a place holder
     ```css
       ::placeholder {
            color: red;
         }
     ```

  1. put in autofill of email on input.cgi
     - <input id="user-text-field" type="email" autocomplete="username"/>
     - <input id="password-text-field" type="password" autocomplete="current-password"/>


  1. put in autofill of email/password for index.cgi
     - these allowing security for prompt setting to work


  1. Modify username to be github account or @my.csun.edu

  1. update tags to be valid XHTML, e.g., <input  > ==> <input />

  1. Mode is not technically correct
     - The mode is a set of values.  All values within the set have the same number of occurrances.  As such, if all values are mutually exclusive the MODE is the universal set.  We have set it to Zero.

participation/  (Draw this up)
   start  <-- provides QR codel, input for prompts, links to other pages
        <QR Code>  <current-class>
   info  < the bottom half of the current index.html
      current-class
      this weeks class
      past classes
   input < as is

   thankyou page --> info pag
       current-class, with autorefresh

   out of -session page -> info page full


### Documentation

### Features
  
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


### Future Feature Consideration
  1. Faculty member wants students to authenticate
     - allow authentication via their @my.csune.du address



