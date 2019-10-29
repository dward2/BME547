# Heart Rate Sentinel Server
This assignment will have you build a simple centralized heart rate sentinel 
server. This server will be built to receive GET and POST requests from mock 
patient heart rate monitors that contain 
patient heart rate information over time. If a patient exhibits a tachycardic 
heart rate, the physician should receive an email warning them of the
situation. So if a new 
heart rate is received for a patient that is tachycardic, the email should be 
sent out at that time. The tachycardic calculation should be based on age 
(more info [here](https://en.wikipedia.org/wiki/Tachycardia); you can assume 
all patients will be one year old or older). The notification e-mail can 
be sent using the free [Sendgrid API](https://sendgrid.com/) (there is a 
[Sendgrid python package](https://github.com/sendgrid/sendgrid-python) that 
wraps the API).  More information on setting up SendGrid can be found 
[here](../Resources/WebServices/sendgrid.md).

Assignment repositories will be hosted in GitHub Classroom.  See the 
assignment in Sakai for the link to create a repository.

## Server Specifications

Your Flask web service should implement the following API routes:

* `POST /api/new_patient` that takes a JSON as follows:
  ```
  {
      "patient_id": "1", # usually this would be the patient MRN
      "attending_email": "dr_user_id@yourdomain.com", 
      "patient_age": 50, # in years
  }
  ```
  The patient_id and age will always be numeric, but may be sent in the JSON as 
  either an integer or a string containing an integer.  Your code should be 
  prepared for either.
  This route is called to register a new patient with your server.  This would
  occur when a heart rate monitor is checked out and attached 
  to a particular patient.  This will allow you to initialize a patient in
  your server and be able to accept future heart rate measurements for this 
  patient.  It will always be called before any heart rate data for the patient
  is sent.
   
* `POST /api/heart_rate` that takes a JSON as follows:
  ```
  {
      "patient_id": "1", # usually this would be the patient MRN
      "heart_rate": 100
  }
  ```
  As above, the patient_id may be sent as an integer or a string, and not 
  necessarily the same as was sent in the `new_patient` call.  For example, the
  id might be sent as a string such as `"1501"` in the `new_patient` call, but 
  sent as an integer such as `1501` in the `heart_rate_ call`.  The 
  heart_rate may also be sent as an integer or string containing an integer. 
  The numeric values will only be
  integers, no decimals.  This route should store the sent heart rate
  measurement in the record for the specified patient.  The 
  [current date/time stamp](https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python) 
  of when the POST was received should also be stored with the heart rate
  measurement.  If the posted heart rate is tachycardic for the specified 
  patient and patient age, an e-mail should be sent to the attending physician. 
  This e-mail should include the patient_id, the tachycardic heart rate, and 
  the date/time stamp of that heart rate.
  
* `GET /api/status/<patient_id>`  
  should return a JSON containing the latest heart rate, as an integer, for the
  specified patient, whether this patient is 
  currently tachycardic based on this most recently posted heart rate, and 
  the date/time stamp of this most recent heart rate.  The return JSON
  should look like:
  ```
  {
      "heart_rate": 100,
      "status":  "tachycardic" | "not tachycardic",
      "timestamp": "2018-03-09 11:00:36.372339"  
  }
  ```
   Note that the `status` key should contain either the string `"tachycardic"` or
   `"not tachycardic"`.  The key `timestamp` should contain a `datetime` string.
 
* `GET /api/heart_rate/<patient_id>` should return a list of all the previous 
  heart rate measurements for that patient, as a list of integers.  Timestamps 
  are not required.

* `GET /api/heart_rate/average/<patient_id>` should return the patient's 
  average heart rate, as an integer, of all measurements you have stored for 
  this patient.
 
* `POST /api/heart_rate/interval_average` that takes a JSON as follows: 
  ```
  {
      "patient_id": "1",
      "heart_rate_average_since": "2018-03-09 11:00:36.372339" // date string
  }
  ```
  As above, the patient_id may be sent as an integer or a string, and not 
  necessarily in the same format as previously sent.  The
  heart_rate_average_since will be a datetime string in the format shown.
  This POST should return the average, as an integer, of all the heart rates that have been
  posted for the specified patient since the given date/time.  Note that
  the given time stamp could be any time, and not necessarily the time of a 
  previous heart rate.
  
The server should write to a log file when the following events occur:
* A new patient is registered.  The log entry should include the patient ID.
* A heart rate is posted that is tachycardic.  The log entry should include the 
patient ID, the heart rate, and the attending physician e-mail.

All of the above routes should return an appropriate status code (depending on
the outcome, including when the request was unsuccessful for whatever reason,
for example, when the input JSON is incorrect).

All of the above routes should do input data validation, making sure that
the appropriate keys in JSON inputs exist, and that the data types are
correct.  If the input is incorrect, an error code should be returned.  Also, 
the routes should return the appropriate status codes if a 
request asks for a patient that does not exist.  It is not appropriate for data
validation and error returns from your server be 500 errors caused by exceptions
raised by your server.  You must handle exceptions and return an error code, 
rather than having the server return a 500 error because it had an unhandled 
exception.
  
Be sure to write modular code. This means your handler 
functions for routes should be calling other independent functions as 
frequently as possible. All of those other independent functions 
should be tested. As mentioned above, you should also remember to validate user 
inputs that come 
from `request.get_json()` to ensure the right fields exist in the data and 
that they are the right type. These validations should be written in 
independent, testable functions (example:  `validate_heart_rate_request(r)`).
You do not have to test the flask 
handler functions directly (the functions associated with the `@app.route` 
decorator), assuming that they have limited code and primarily call other
functions to do the work.  All of these other functions should be tested.  

(In other words, your route functions should do nothing more than receive
the input, call other functions, and return the results).

Note: for this assignment, your server will need to keep the information
it is sent.  You can choose to store this information by using an in-memory
data structure like Python lists and dictionaries, or you can choose to use
an external database.

For the attending e-mail:  use an e-mail address that you can check to verify
appropriate function.  When your code is being evaluated for grading, a real 
e-mail address will be used for verification.  

## Submission Notes
- __As always in this class, be sure to follow all best practice conventions 
(unit testing, git practices, Travis CI, virtual environments, PEP8, 
docstrings, descriptive README.md, license, etc)__
- Unit tesing should be done in parallel with code development.  So, when code
is written on a feature branch and merged into master, there must be
appropriate unit testing available during that merge.  You cannot write the
code first, merge it, and then write the tests later.  Any code that is merged
without simultaneous unit testing will be a deduction.
- As discussed below, unit tests are not required for the function that calls 
SendGrid, so keep this function separate and small.
- Create a git tag for the final version of your repository as done previously 
in this class.
- The SendGrid part of this assignment will not be worth the majority of 
points, so focus on that part after the rest of the functionality has been 
completed.
- Deploy your server code on your VCM and include in your README.md file the 
hostname and port on which your server is running (eg., 
`vcm-1000.vm.duke.edu:5000`).  Remember to 
follow the instructions about ensuring your server is not automatically
shut down (there is a check box on the VCM control panel. It will ask you for a 
reason, just say you are running a web server assignment for BME 547 
Medical Software Design). __Please do this deployment step last, it is most 
important to complete the rest of the assignment first (that is where most of 
the points are)__.
- While developing your code, it is likely that you will write up a local
client program to test your server.  While it is your server code and 
associated test functions that will be evaluated, it may also be beneficial to
include your client code in your repository.  If the graders have any issue
with accessing or using your server, seeing how you did it in your client 
could help in their evaluation.  

## More information about SendGrid
You need to create a free account at [sendgrid.com](https://sendgrid.com) and 
then create an API key which is a key that authenticates you to use the 
SendGrid API. Keys can be created either by following the procedures given at 
<https://sendgrid.com/docs/ui/account-and-settings/api-keys/#creating-an-api-key>
or using the Startup Guide as described at 
[sendgrid.md](../Resources/WebServices/sendgrid.md).  Note that 
SendGrid has a nice [python API](https://github.com/sendgrid/sendgrid-python) 
that you can install using pip. In the 
[example code shown there](https://github.com/sendgrid/sendgrid-python#quick-start), 
you need to set the `SENDGRID_API_KEY` environment variable to your API key 
you created earlier. Do not commit your key to GitHub in either a file or 
hard-coded into your python code.  That will expose 
it for others to use, and SendGrid has been known to scan the web for exposed
keys and cancel accounts for keys it finds in order to avoid hackers/spammers 
from using their system.  More detailed information on setting up your API Key
and `sendgrid` can be found [here](../Resources/WebServices/sendgrid.md).

NOTE:  For this assignment, unit tests for your function that sends e-mail
using SendGrid are not required as that would require sending your API key to
Travis.  While there are secure ways of doing so, it is not a topic for this
class.

### Special note for Mac users
:eyes: Apparently python 3.6 and higher for Mac does not come configured to use the 
standard root certificate authorities, so some folks may get a ssl error when 
using the SendGrid client. To fix this, run the following command:

```
/Applications/Python\ 3.6/Install\ Certificates.command
```

If you installed Python 3.7, change 3.6 to 3.7 in the command above.

If you're getting an error like this in conda, try 
```sh
conda remove certifi
conda install certifi
```