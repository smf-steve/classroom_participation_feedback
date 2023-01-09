### New Layout

home
  index.html
  input.html
  not-in-session.html
  summaries.html  (iframe summaries.cgi)


  admin:
    index.cgi
    init_report.cgi
  cgi:
    input.cgi
    logger.cgi
  etc:
    class_info
    participation.env
    response_filter.sed

  bin:
    individual_report2html
    report2html
    log2report

index.html
input.html
not-in-session.html
summaries.html

admin/index.cgi*
admin/init_report.cgi*

bin/individual_report2html*
bin/report2html*
bin/log2report*

cgi/input.cgi*
cgi/logger.cgi*
cgi/class_responses.cgi*


etc/class_info
etc/participation.env
etc/response_filter.sed




index.html:  redirect to index.cgi
   1. DirectorIndex does not work on csun?
      -- or make steps to make it work

index.cgi:
   1. a web page that contains
      - two columns
        1. QR Code and Input Information
           - posts to init_report.cgi
        1. Current class feedback (iframe: (class_response.cgi))
   1. Use .htaccess to allow authentication
   1. Contains links to:
      1. QR Code to got to input.cgi
      1. History of responses

init_report.cgi:
   1. used to init a report for the current session
   1. redirects back to index.cgi


input.cgi:
   1. a mobil page that conatins  input information
      1. single column
   1. posts to logger.cgi

logger.cgi:
   1. records students response
   1. redirects to
      * class_responses.cgi or 
      * not-in-session.html -->
        - reports.cgi  (implies the page should be mobil friendly)

class_responses.cgi:
   1. a mobil page for the current responses
   Bugs:
     - remove prompt outside of the text box
     - add scale rating

not-in-session.html
   1. simple web-page to state the class is not in session

summary.cgi:
   1. a web page that 
      - Nav list for list of sessions
      - Row of class info
        - two columns
          1. Graph
          1. responses


## Notes:
   Place .htaccess in place and test
   Update index.cgi to initializ th report 
   Test on CSUN infractructure, note possible issue with 
     -- X=( ${LOGS}/\*.log )                 # run `ls` command
     -- X=( $( echo ${LOGS}/\*.log )                 # run `ls` command



### Bugs
  1. Add HTaccess authentication for Faculty member on index.cgit
     - this is to allow the update of response prompts
  1. Update the init_report.cgi to require authentication
  1. Should the 2:00 class appear before or after the 9:00 class... (i.e. sort by military time)

  1. Heading Values (e.g., Prompt) should be bolded to allow them to stand out more

  * input.cgi
    1. in dark mode, the slide range is not apparent
     - should the slide provide the value selected. 

### Things to do
  1. Place rating in the line of the feedback
     Rating:  Feedback:  (maybe the individual ratings are not important. you can see it on the graph!)
     ``5  | 1. This is some feedback``
     ``-- | 2. This is some feedback``
     ``10 | 3. This is some feedback``
     last two lines: 
       `` ``
       ``Ratings: Count=#; Mode=; Median; Average=; etc.``
  1. Restructure the filesystem for proper placement of public and nonpublic files

  1. move all code to bin
     - only have front pages at the top?

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



### Presentation and CSS 
  1. Put a repo link on the index.html page

  1. modify the text of the Class Coverage placeholder to render not as a place holder
     ```css
       ::placeholder {
            color: red;
         }
     ```

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


  1. The Class Description should be placed into readonly textarea... ?
     Ditto for the feedback
     This will unify the way it looks?


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

   

### Future Feature Consideration
  1. Faculty member wants students to authenticate
     - allow authentication via their @my.csun.edu address

  1. Determine if we need to delay the immediate publication on feedback
     - so far no issues, but what if something "inappropriate" is posted.
     - could add a filter (akin to response_filter.sed), that blocks out a line in which any "inappropriate" words are used.

  1. rewrite the protoype in an appropriate MVC web langauge

  1. Create a QR code on the fly with an embedded code 
     1. to limit spruious usage of the system
     1. to encode class session information (reduce the number of fields to post)

