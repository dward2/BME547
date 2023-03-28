# Patient Lab Test Results Server
This assignment will have your team build a simple, centralized patient test
results server.  This server will be built to receive GET and POST requests
from two general types of users:
* Physician: can enter patient information, order tests, and get test
results
* Lab technician: can get what tests were ordered and upload the results of
tests

The server should store the data it is sent so that it can be recalled as 
needed.

## Server Specifications

### Routes
Your Flask server should implement the following routes.

* `POST /patient/new_patient` that allows information about a new patient to be
  added to the server.  It should accept JSON input as follows:
    ```
      {
          "patient_mrn": <medical_record_number>,
          "attending_email": <attending_email>, 
          "patient_age": <patient_age>
      }
    ```
   where
  * `<medical_record_number>` is the unique medical record number for the 
  patient (see the section below entitled **Medical Record Number and Age 
  Data Types** for more information on expected data types for this value)
  * `<attending_email>` is a string containing an e-mail address
  * `<patient_age>` is the patient's age in years (see the section below
  entitled **Medical Record Number and Age Data Types** for more information
  on expected data types for this value)
    
  The e-mail address provided here will be used to send notifications to the
  attending physician if any test results come back as abnormal.  While the
  e-mail address should be of the correct syntax (i.e., name@domain.com), it
  does not need to be an active e-mail address as we will be using a simulated
  email system for this assignment.  For the e-mail address, the server only 
  needs to validate that it is a string.  It does not need any validation of
  the format.

* `POST /patient/new_request` allows the attending physician to request that a
  test be performed on a patient.  It takes a JSON as input as follows:
    ```
      {
          "patient_mrn": <medical_record_number>,
          "test_name": <test_name>
      }
   ```
  where
  * `<medical_record_number>` is the patient medical record number 
  (see the section **Medical Record Number and Age Data Types** below for
  information on the expected data types for this value)
  * `<test_name>` is the name of the test be requested

  The received request should be stored on the server so that the lab can see
  what tests have been requested.  A date/time stamp should be stored with the
  request.  An e-mail should then be sent to
  the lab.  The email should be "from" the attending physician, "to" the lab,
  the subject line should contain the patient medical record number and test 
  name, and the body of the email should contain the patient medical record
  number, test name, and the request date/time.  Information on how to send
  the e-mail is provided below.  

* `POST /lab/email_address` registers the e-mail address of the lab with the
  server.  It takes a JSON input as follows:
    ```
      {
          "email": <email_address>
      }
    ```
  where:
  * `<email_address>` is a string containing the e-mail address of the lab

  The e-mail address will be used to send new requests when uploaded to the
  server.  As above, it should be a correct e-mail address (such as 
  `lab@hospital.com`) but does not need to be an active e-mail.

* `GET /lab/list_available_tests` returns a list of strings that contains the
names of available tests.  Available tests should include:
  * `"HR"` for a heart rate
  * `"HDL"` for HDL
  * `"LDL"` for LDL
  * `"TSH"` for thyroid-stimulating hormone

* `GET /lab/open_requests` returns information about test requests that have
been submitted to the server but not yet been completed.  This route should
return a list where each entry in the list is a dictionary representing a
single test request.  This dictionary should be formatted as follows:
  ```
    { 
       "patient_mrn": <medical_record_number>,
       "test_name": <test_name>,
       "request_date": <request_date_time>
    }  
  ```
  where:
  * `<medical_record_number>` is an integer containing the patient medical
  record number
  * `<test_name>` is a string containing the name of the test to be performed
  * `<request_date>` is a string containing the date/time stamp of when the
  request was received.  It should be in the format as shown by this
  example:  `2018-03-09 11:00:36`
  
  If there are no uncompleted test requests, an empty list should be returned.

* `POST /lab/new_result` allows the lab to post new test results to the server.
  It takes a JSON input as follows:
  ```
    { 
       "patient_mrn": <medical_record_number>,
       "test_name": <test_name>,
       "test_result": <test_result>
    }  
  ```
  where:
  * `<medical_record_number>` is the patient medical record number (see the
  section **Medical Record Number and Age Data Types** below for more info)
  * `<test_name>` is the name of the test performed
  * `<test_result>` is a numeric value (`int` or `float`) with the result of
  the test

  The server should store this lab result along with the date/time stamp of
  when the result was received.  The request for this test for this patient
  should be removed from the database.  There will only be
  one open request per test type per patient at any given time.  

  The server should also examine the results of the test.  If the result is 
  "abnormal", an email should be sent to the attending physician.
  The email should be sent "to" the attending, "from" the lab, the
  subject line should include the patient medical record number, the test name, 
  and "Abnormal result".  The body should contain the patient medical record
  number, the test name, the actual result value,
  and the date/time that the test was completed.   

  Abnormal results are considered as follows:
  * For `"HR"`, an abnormal result is when the heart rate is tachycardic.  The
  heart rate above which is tachycardic varies by age.  Use the ranges as given
  at <https://en.wikipedia.org/wiki/Tachycardia> under the "Diagnosis" heading.
  All ages will be at least 1-year-old, so ignore the levels for less than 
  1-year-old.  
  * For `"HDL"`, a value of less than 60 is considered abnormal.
  * For `"LDL"`, a value of 130 or greater is considered abnormal.
  * For `"TSH"`, a value less than 1.0 or greater than 4.0 is considered
    abnormal.  (In other words, a value of 1.0 to 4.0 inclusive is considered
    normal.)

* `GET /patient/results/<patient_mrn>` retrieves information about a patient.
  The variable URL contains the medical record number of the patient to be
  retrieved.  The route 
  returns a JSON-encoded string that contains a dictionary with the
  following information:
  ```
    { 
       "patient_mrn": <medical_record_number>,
       "completed_tests": <list_of_test_dictionaries>,
       "open requests": <list_of_request_dictionaries>
      }  
  ```
  where:
  * `<medical_record_number>` contains an integer with the patient's medical 
  record number
  * `<list_of_test_dictionaries>` contains a list of dictionaries where each
  dictionary contains information about the results of a single test.  Its
  format is described below.
  * `<list_of_request_dictionaries>` contains a list of dictionaries where
  each dictionary contains information about an open test request.  Its format
  is described below.

  If there are no completed tests or no open test requests for a patient, the
  corresponding list should be an empty list.

  The test dictionaries should look like this:
    ```
      { 
         "test_name": <test_name>,
         "test_result": <test_result>,
         "status": <status_string>
         "timestamp": <datetime_stamp>
        }  
    ```
  where:
  * `<test_name>` is a string containing the name of the test
  * `<test_result>` is a numeric value, either an `int` or `float`, containing
  the result of the test
  * `<status_string>` is a string that is either `Abnormal` or `Normal`
  depending on the value of the test
  * `<datetime_stamp>` is a string containing the date/time stamp of when the
  test result was received by the server.  It should be in the format as shown 
  by this example:  `2018-03-09 11:00:36`
  
  The open request dictionaries should look like this:
    ```
      {
         "test_name": <teste_name>,
         "request_timestamp": <datetime_stamp>
      }
    ```
  where:
  * `<test_name>` is a string containing the name of the test
  * `<datetime_stamp>` is a string containing the date/time stamp of when the
  test request was received by the server.  It should be in the format as shown 
  by this example:  `2018-03-09 11:00:36` 

* `GET /patient/results/<patient_mrn>/<test_name>` returns a list of all 
  available test results for the specified type of test for the specified 
  patient.  The `<patient_mrn>` portion of the URL should contain the medical
  record number of the patient of interest.  The `<test_name>` portion of the
  URL should contain the test name of interest.  
  This route should return a list of numeric values (not numeric strings).  If 
  there are no results for the specified test for the specified patient, the
  route should return an empty list.

* `GET /patient/results/<patient_mrn>/<test_name>/average` returns a float that
  is the average result for all available tests of the specified type for the
  specified patient.  The `<patient_mrn>` portion of the URL should contain the 
  medical record number of the patient of interest.  The `<test_name>` portion 
  of the URL should contain the test name of interest.  If the specified 
  patient does not have any results for the specified test, a status code of
  400 should be returned along with an appropriate message.

* `POST /patient/results/interval_average` returns a float that is the average
  result of all available tests of the specified type that were received after
  a specified date/time for the specified patient.  This route takes a JSON 
  input as shown:
  ```
    {
        "patient_mrn": <medical_record_number>,
        "test_name":  <test_name>,
        "average_since": <date_time_stamp>
  ```
  where:
  * `<medical_record_number>` is the patient medical record number
  * `<test_name`> is a string containing the name of the test of interest
  * `<date_time_stamp>` is a string containing a date/time in the format given
  in this example:  `2018-03-09 11:00:36`
  
  This route should find test results for the specified patient for the
  specified test and average only those results that were received at or after
  the given date/time stamp.  Note that the given date/time stamp could be 
  any time and not necessarily the date/time of any given test.  This average
  should be returned as a float. If the specified patient does not have any 
  results for the specified test at or after the specified date/time, a status
  code of 400 should be returned with an appropriate message.

#### Medical Record Number and Age Data Types
The actual medical record number and age for a patient will always be an 
integer.  However, the value `<medical_record_number>` or `<patient_age>` in 
any of the JSON input 
dictionaries above might be an integer, a numeric string, or a string with
letters and numbers.  Your code must be prepared to parse this input and
determine whether the input is acceptable (can it be
turned into an integer) or rejected (if it contains any letters).  So, 
* `123` or `"123"` should be accepted (although the 
  string `"123"` should be converted into the integer  `123` for storage)
* `"a54"`, `"aj"`, or `"54a"` should be rejected.

Note that you cannot assume that a medical record number or age will always
be sent in one form or another.  For example, when a patient with the medical
record number of 1501 is sent to the `patient/new_patient` route, the medical
record number might be sent as a string such as `"1501"`.  Then, in a following
request to the `patient/new_request` route, the integer `1501` might be sent.
So, you must always check that the medical record number or age input is 
acceptable or not, regardless of whether it was before.

### Validation
All POST routes should perform validation of the input JSON to ensure that the
needed keys exist and the value types are correct.

All routes that are sent a medical record number (either in POST requests or
as part of a variable URL), except the 
`patient/add_patient` route, should validate that the given medical record 
number exists in the database.  

All routes that are sent a test name (either in POST requests or
as part of a variable URL) should validate that the test name matches
one of the defined test names.  

All routes that are sent an e-mail address only need to validate that the
value sent is a string.  Specific validation of the e-mail format is not
required.  

Routes that are sent a date/time stamp as a string only need to validate that
the date/time stamp is a string.  It does not need to validate that the
date/time format of the string is correct.  (Of course, make sure any client
code you write does send a string with the correct format or else your
server may not work properly.)

All routes should return an appropriate status code depending on the outcome.
For example, successful requests should return a 200 status code.  Requests
that are unsuccessful for any reason (including, but not limited to, when the 
input JSON validation fails or a patient doesn't exist in the database) should 
return a 400 (or other 
appropriate non-2xx) status code.  A descriptive message of the problem should 
also be returned.

It is never appropriate for a route to return an "Internal Server Error"
response and a 500 status code.  You must handle all exceptions on the server
side and return a non-500 error code with a message, rather than having the 
server return a 500 error because it had an unhandled exception.

### Logging
The server should write to a log file when the following events occur:
* A new patient is added.  The `Info` log entry should include the patient 
  medical record number and the attending e-mail address.
* A new test result is abnormal.  The `Warning` log entry should include the 
  patient medical record number, the test name, the test result, the fact that 
  it is abnormal, and the attending e-mail address to which an email was sent.

### Data Storage
For this assignment, your server will need to keep the information it is sent.
You can choose to store this information using an in-memory data structure
like lists, dictionaries, or classes.  You could also choose to use an
external database.

### E-mail Server
I have set up a server to simulate accessing a third-party webservice for 
sending e-mails.  When your program needs to send an e-mail, it should make
a POST request to the following URL:
```
http://vcm-7631.vm.duke.edu:5007/send_email
```
**NOTE**: The port is `5007`.  

This POST request should be sent a JSON with the
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

## Modular Code & Testing
Be sure to write modular code.  This means your Flask handler functions should
have minimal code in them.  It should be limited to getting any data sent with
the request, calling other functions to do the work, and then returning the
response.  All other functions that are called should be written in such a way
that they can have comprehensive unit tests.  The Flask handler functions do
not need unit tests if you write them as described.  

## Working As A Team
* Schedule a planning meeting with your team.
* One member of the team is responsible for implementing the following routes:
  * `/patient/new_patient`
  * `/patient/new_request`
* The other member of the team is responsible for implementing this route:
  * `/lab/new_result`
* As a team, decide which member will handle which of the above.
* Next, agree on who will be primarily responsible for these remaining routes.  
  * `/patient/results/<patient_mrn>`
  * `/patient/results/<patient_mrn>/<test_name>`
  * `/patient/results/<patient_mrn>/<test_name>/average`
  * `/patient/results/interval_average`
  * `/lab/open_requests`
  * `/lab/email_address`
  * `/lab/list_available_tests`
* For all of the above routes, open a GitHub issue for each route and assign 
  it to the responsible party 
  (this will document who has primary responsibility for each route).  
* As a team, agree on a basic structure for how to store the data.  Open a 
  GitHub Issue and describe, in detail, how the data will be stored.  For 
  example, if the patient data will be stored in a dictionary, write out the
  specific format for the dictionary.  
* As desired, discuss and document in GitHub Issues any other design decisions 
  for the server.

The above steps must be completed and documented by GitHub Issues by the first 
deadline as outlined in the
Sakai assignment.  _If you complete these items before the deadline, which is
highly recommended, please notify me for my review._

During my evaluation of your submission, I will be looking at commit
histories to determine that both team members contributed to the project
appropriately.  Feel free to work together, help each other, and edit and debug
each other's code.  But, make sure that each team member is contributing and
committing to their assigned routes as documented in the GitHub Issues.    

## Submission Notes
- __As always in this class, be sure to follow all best practice conventions 
(unit testing, git practices, GitHub Actions CI Integration, virtual 
  environments, PEP8, docstrings, descriptive README.md, license, etc)__
- Unit testing should be done in parallel with code development.  So, when code
is written on a feature branch and merged into main, there must be
appropriate unit testing available during that merge.  You cannot write the
code first, merge it, and then write the tests later.  Any code that is merged
without simultaneous unit testing will lead to a deduction.
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
