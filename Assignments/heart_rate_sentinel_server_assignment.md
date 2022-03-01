# Heart Rate Sentinel Server
This assignment will have your team build a simple centralized heart rate 
sentinel server. This server will be built to receive GET and POST requests 
that contain patient heart rate information from mock patient heart rate 
monitors.  This server should store this data so that patient information 
over time can be recalled.  When the server receives a tachycardic heart rate 
for a patient, the physician should receive an email warning them of the
situation. So if a new 
heart rate is received for a patient that is tachycardic, the email should be 
sent out at that time. The tachycardic calculation should be based on age 
(more info [here](https://en.wikipedia.org/wiki/Tachycardia); you can assume 
all patients will be one year old or older). A system for sending the e-mails
is described below.

The server will also have routes that allow physicians to register on the
server and provide their contact information.

Assignment repositories will be hosted in GitHub Classroom.  See the 
assignment in Sakai for instructions to create a team repository.

## Server Specifications

### Routes
Your Flask web service should implement the following API routes.  Please note
that the `/api` at the start of the routes given below should be included
in your route name.

* `POST /api/new_attending` that takes a JSON input as follows:
  ```
  {
      "attending_username": <attending_username_string>,
      "attending_email": <attending_email_string>, 
      "attending_phone": <attending_phone_string>
  }
  ```
  where
  + `<attending_username_string>` is a string in the format 
    "LastName.FirstInitial" such as `"Smith.J"`
  + `<attending_email_string>` is a string containing an e-mail address such
    as `"DrSmith@my_hospital.com"`
  + `<attending_phone_string>` is a string containing a 10 digit phone number
    such as `"919-555-1212"`
    
  The e-mail provided here will be used to send notifications to the physician
  that is registered for each patient.  While the e-mail should be of the
  correct syntax (i.e., name@domain.com), it does not need to be an active
  e-mail address as we will be using simulated email system for this 
  assignment.  The value for the
  `"attending_username"` key will be used in the `api/new_patient` route below 
  for linking a patient with an attending physician.  
  
* `POST /api/new_patient` that takes a JSON input as follows:
  ```
  {
      "patient_id": <patient_id>,
      "attending_username": <attending_username_string>, 
      "patient_age": <patient_age>, # in years
  }
  ```
  where
  + `<patient_id>` is the patient medical record number.  The actual medical
    record number will always be an integer.  However, the value sent as the 
    `<patient_id>` value in the above dictionary may contain integers, numeric 
    strings, or a string with letters and numbers.  Your code must be prepared
    to parse this input and determine whether the id is acceptable (i.e.,
    can be turned into an integer) or rejected (if it contains any letters).
    So, `123` or `"123"` should be accepted as patient_ids (although the string 
    `"123"` should be converted into the integer `123` for storage), while 
    `"a54"`, `"aj"`, or `"54a"` should be rejected.
  + `<attending_username_string>` is a string following the 
    "LastName.FirstInitial" format as described in the `/api/add_attending` 
    route above.
  + `<patient_age>` is the patient's age in years.  The actual age will always
    be an integer, but as with the `<patient_id>`, the value in the dictionary 
    may be an integer, numeric string, or a string with letters and numbers.
    Again, your code must distinguish between acceptable and unacceptable
    inputs.
    
  This route is called to register a new patient with your server.  This would
  occur when a heart rate monitor is checked out and attached 
  to a particular patient.  This will allow you to initialize a patient in
  your server and be able to accept future heart rate measurements for this 
  patient.  The `"attending_username"` key contains a string that will be used 
  to match with an attending physician as described in the `/api/add_attending`
  route.
   
* `POST /api/heart_rate` that takes a JSON as follows:
  ```
  {
      "patient_id": <patient_id>,
      "heart_rate": <heart_rate>
  }
  ```
  where
  + `<patient_id>` is the patient medical record numbers
  + `<heart_rate>` is the patient heart rate being recorded.
  
  As with the `/api/new_patient` route, the `<patient_id>` or `<heart_rate>`
    values may be sent as an integer, a string containing an integer, or a 
    string containing numbers and letters.  And, it may not 
  necessarily be the same as was sent in the `/api/new_patient` call.  For 
  example, the
  id might be sent as a string such as `"1501"` in the `new_patient` call, but 
  sent as an integer such as `1501` in the `heart_rate` call.  Integers and
    numeric strings should be accepted.  Strings of mixed numbers and integers
    should be rejected.  The 
  actual heart rate will only be integers, not decimals.  
  
  This route should store the sent heart rate
  measurement as an integer in the record for the specified patient.  The 
  [current date/time stamp](https://github.com/dward2/BME547/blob/main/Assignments/time_server_project.md#getting-current-datetime) 
  of when the POST was received should also be stored with the heart rate
  measurement.  If the posted heart rate is tachycardic for the specified 
  patient and patient age, an e-mail should be sent to the attending physician
  whose e-mail address was registered in the `api/add_attending` route. 
  This e-mail should include the patient_id, the tachycardic heart rate, and 
  the date/time stamp of that heart rate.
  
* `GET /api/status/<patient_id>`  
  should return a dictionary in a JSON string containing the latest heart rate, 
  as an integer, for the specified patient, whether this patient is 
  currently tachycardic based on this most recently posted heart rate, and 
  a string containing the date and time of this most recent heart rate 
  formatted as shown in the example below.  
  The return dictionary/JSON string should look like:
  ```
  {
      "heart_rate": <heart_rate_integer>,
      "status":  <status_string>, 
      "timestamp": <time_stamp_string>   
  }
  ```
  where
  + `<heart_rate_integer>` the most recent heart rate as an integer 
    (ex., `100`)
  + `<status_string>` is either the string `"tachycardic"` or 
    `"not tachycardic"` based on the most recent heart rate,
  + `<time_stamp_string>` is a string indicating the date/time of the most
    recent heart rate.  It should be in the format as shown by the example
    "2018-03-09 11:00:36".
 
* `GET /api/heart_rate/<patient_id>` should return a list of all the previous 
  heart rate measurements for that patient, as a list of integers.  Timestamps 
  are not required.  The list should be returned as a JSON string.

* `GET /api/heart_rate/average/<patient_id>` should return the patient's 
  average heart rate, as an integer, of all measurements you have stored for 
  this patient.  The integer should be returned as a JSON string.
 
* `POST /api/heart_rate/interval_average` that takes a JSON as follows: 
  ```
  {
      "patient_id": <patient_id>,
      "heart_rate_average_since": <time_stamp_string>
  }
  ```
  where
  + `<patient_id>` is the patient medical record number,
  + `<time_stamp_string>` is a string containing a date/time following the
  format as shown by the example "2018-03-09 11:00:36".  
  As above, the patient_id may be sent as an integer or a string, and not 
  necessarily in the same format as previously sent.  The
  heart_rate_average_since will be a string containing a date and time in the 
  format shown.
  This POST should return the average, as an integer, of all the heart rates that have been
  posted for the specified patient since the given date/time.  Note that
  the given time stamp could be any time, and not necessarily the time of a 
  previous heart rate.  The integer average should be returned as a JSON string.
  
* `GET /api/patients/<attending_username>` returns information on all the 
patients of the attending physician with the given `attending_username`.  This
route should return a list of dictionaries, in a JSON string, where each 
  dictionary in the list represents data from a patient of this physician.  
  The patient dictionaries should be in the following format:
  ```
  {
      "patient_id": <patient_id>,
      "last_heart_rate": <heart_rate_integer>,
      "last_time": <time_stamp_string>,
      "status": <status_string>
  }
  ```
  where
  + `<patient_id>` is the patient medical record number,
  + `<heart_rate_integer>` the most recent heart rate as an integer 
    (ex., `100`)
  + `<time_stamp_string>` is a string containing a date/time following the
  format as shown by the example "2018-03-09 11:00:36",  
  + `<status_string>` is either the string `"tachycardic"` or 
    `"not tachycardic"` based on the most recent heart rate.
 
  If no patients exist for a physician, an empty
   list should be returned.  If the `attending_username` does not exist in the
   database, an appropriate error should be returned.

### Logging   
The server should write to a log file when the following events occur:
* A new attending physician is registered.  The log entry should include the
attending username and e-mail.
* A new patient is registered.  The log entry should include the patient ID.
* A heart rate is posted that is tachycardic.  The log entry should include the 
patient ID, the heart rate, and the attending physician e-mail.

### Status Codes & Data Validation
All the above routes should return an appropriate status code depending on
the outcome.  For example, successful requests should return a 200 status code.
Request that are unsuccessful (for example, when the input JSON is incorrect)
should return a 400 (or other appropriate) status code.

All the above routes should do input data validation, making sure that
the appropriate keys in JSON inputs exist, and that the data types are
correct.  If the input is incorrect, a non-2xx status code should be returned.  

Also, the routes should return the appropriate status codes if a 
request asks for a patient that does not exist.  It is not appropriate for data
validation and error returns from your server be 500 "Internal Server Error" 
codes caused by exceptions
raised by your server.  You must handle exceptions and return a non-500 error code, 
rather than having the server return a 500 error because it had an unhandled 
exception.

### Modular Code & Testing  
Be sure to write modular code. This means your handler 
functions for routes should be calling other independent functions as 
frequently as possible. All of those other independent functions 
should be tested. As mentioned above, you should also remember to validate user 
inputs that come 
from `request.get_json()` to ensure the right fields exist in the data and 
that they are the right type. These validations should be done in 
functions that can be tested.

You do not have to test the flask 
handler functions directly (the functions associated with the `@app.route` 
decorator), assuming that they have limited code and primarily call other
functions to do the work.  All of these other functions should be tested.
(In other words, your route functions should do nothing more than receive
the input, call other functions, and return the results).

### Data Storage
For this assignment, your server will need to keep the information
it is sent.  You can choose to store this information by using an in-memory
data structure like Python lists, dictionaries, or classes.  You could also
choose to use an external database.

### E-mail Server
I have set up a server to simulate accessing a third-party webservice for 
sending e-mails.  When your program needs to send an e-mail, it should make
a POST request to the following URL:
```
http://vcm-7631.vm.duke.edu:5007/hrss/send_email
```
**NOTE**: The port is `5007`.  This POST request should be sent a JSON with the
following dictionary contents:
```
{
 "from_email": <from_email_str>,
 "to_email": <to_email_str>,
 "subject": <subject_str>,
 "content": <content_str>
}
```
where `<from_email_str>` is a string containing the e-mail address from which
the message is being sent, `<to_email_str>` is a string containing the e-mail
address to which the message is being sent, `<subject_str>` is a string
containing the subject of the e-mail, and `<content_str>` is a string 
containing the content of the e-mail.

If the request is successful, a string will be returned indicating that the
e-mail was sent and the from and to address.  The status code will be 200.

If the request is bad (i.e., there is a problem with the dictionary being sent, 
or the e-mail addresses in it), a status code of 400 will be returned along
with a string describing the error.

If you have the code to call the e-mail server in its own modular function, you
do not need to have a unit test for that function.

## Working As A Team
Start by having a planning meeting with your team.
One member of the team is responsible for implementing the `/api/new_patient`
route while the other member of the team is responsible for implementing the
`/api/new_attending` route.  As a team, decide which member will handle which
of those two routes, and then agree on who will be primarily responsible
for the remaining routes.  For each route, open a GitHub issue and assign it
to the responsible party (this will document who has primary responsibility for
each route).  You will also need to agree on a basic structure for how to
store the data and any other design decisions for the server.  Consider opening
GitHub Issues, or adding comments to existing issues, that document these
decisions so that both team members have access to them.

During my evaluation of the final submission, I will be looking at commit
histories to determine that both team members contributed to the project
appropriately.  Feel free to work together, help each other, and edit and debug
each other's code.  But, make sure that each team member is contributing and
committing to their assigned routes.    

## Submission Notes
- __As always in this class, be sure to follow all best practice conventions 
(unit testing, git practices, GitHub Actions CI Integration, virtual 
  environments, PEP8, docstrings, descriptive README.md, license, etc)__
- Unit testing should be done in parallel with code development.  So, when code
is written on a feature branch and merged into main, there must be
appropriate unit testing available during that merge.  You cannot write the
code first, merge it, and then write the tests later.  Any code that is merged
without simultaneous unit testing will be lead to a deduction.
- Create a git tag for the final version of your repository as done previously 
in this class.
- Deploy your server code on your virtual machine and include in your README.md 
file the hostname and port on which your server is running (e.g., 
`vcm-1000.vm.duke.edu:5000`).  Remember to 
follow the instructions about ensuring your server is not automatically
shut down (There is a checkbox on the VCM control panel. It will ask you for a 
reason, just say you are running a web server assignment for BME 547 
Medical Software Design). __Please do this deployment step last.  It is most 
important to complete the rest of the assignment first (that is where most of 
the points are)__.
- While developing your code, it is likely that you will write up a local
client program to test your server.  While it is your server code and 
associated test functions that will be evaluated, it may also be beneficial to
include your client code in your repository.  If the graders have any issue
with accessing or using your server, seeing how you did it in your client 
could help in their evaluation.  

### Special note for Mac users
:eyes: Apparently python 3.6 and higher for Mac does not come configured to use the 
standard root certificate authorities, so some folks may get a ssl error, other
error, or just not be able to reach certain web services, such as MongoDB. 

Please visit <a href="../Resources/installations_mac.md">Resources/installations_mac.md</a>
for possible fixes.