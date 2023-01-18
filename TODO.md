### New Layout

  * index.cgi
  * not-in-session.html
  * admin/index.cgi
  * admin/init_report.cgi
  * bin/report2html
  * bin/log2report
  * cgi/input.cgi
  * cgi/logger.cgi
  * etc/class_info
  * etc/participation.env
  * etc/response_filter.sed

  * logs
  * reports


## Notes:
   Place .htaccess in place and test
   Test on CSUN infractructure, note possible issue with 
     -- X=( ${LOGS}/\*.log )                 # run `ls` command
     -- X=( $( echo ${LOGS}/\*.log )                 # run `ls` command

   Create a process to create images of the charts and load as images -- this is optimization only
     -- this should spead up the processing of renderting charts
     -- alternativel, place the current in-session one in a iframe, and only have that Iframe refresh



### Bugs
  1. Add HTaccess authentication for Faculty member on index.cgit
     - this is to allow the update of response prompts
  1. Update the init_report.cgi to require authentication
  1. Should the 2:00 class appear before or after the 9:00 class... (i.e. sort by military time)

  1. .frame width needs to be done the right way.
  1. .frame margin at the bottom to tighten up ratings.
  1. Heading Values (e.g., Prompt) should be bolded to allow them to stand out more
  1. A chart that has no data, generates a error..

     - should the slide provide the value selected. 

  1. the CSS stuff does not seem to be loading correctly...

  1. class_responses.cgi
     - update to be mobil
     - remove the chart
     - scroll to the bottom
  1. admin/index.cgi
     - repostion the boxes
     - present the charrt
     - scroll to the bottom
  1. home/index.cgi
     - add link to the repo
     - provide description
     - add a list of the classes that are under review
     - add the ability to sort based upon a class...

  1. consequence off setting to the end of the <ol> on reload cause you to lose your place in reviewing the file 
     - maybe this is just on large ... files

  1. placing the :party_parrot: or UTF-8 chars into admin/index
     - place the right stuff into the reports, etc.
     - however, it does not redener correctly into the input-boxes. correctly.
     - still an issue with the reload of the page..
      * perhaps update reload on the first submit 
      * perhaps making the top part a frame.
  1. the Class Coverage box on cgi/class_response, should not be a text input box but a html redering box
  
  1. On submit..
     - if any field is not empty, then
       * values are all set to the original
       * then update the one that is not empty
     - if all are empty, then reset to the defaults

### Things to do
  1. Place rating in the line of the feedback
     Rating:  Feedback:  (maybe the individual ratings are not important. you can see it on the graph!)
     ``5  | 1. This is some feedback``
     ``-- | 2. This is some feedback``
     ``10 | 3. This is some feedback``
     last two lines: 
       `` ``
       ``Ratings: Count=#; Mode=; Median; Average=; etc.``


  1. refresh on admin/index.cgi  needs to be only on the chart part

  1. Determine what other types of re-encoding needs to be performed on student responses
     - For example:
       * Student feedback: lots of info provided%2C need to review to understand completely
       * Published feedback: lots of info provided, need to review to understand completely
       * See: https://www.tutorialspoint.com/html/html_url_encoding.htm

  1. Add the ability to add emojis for feedback, like party parrot



### Presentation and CSS 
  1. Put a repo link on the index.html page


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

