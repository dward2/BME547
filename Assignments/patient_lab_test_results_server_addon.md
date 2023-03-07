# Patient Lab Test Results Server Administrator Function
* `POST /admin/new_administrator` allows for the registration of a new
  administrator account.  It takes a JSON input as follows:
    ```
      {
          "admin_username": <username>,
          "admin_password": <password>
      }
    ```
  where
  * `<username>` is a string containing the username of the new administrator
  * `<password>` is a string containing the password of the new administrator

  Neither the username nor password strings should be empty strings.  If either
  one is, a 400 status code with appropriate message should be returned.

  The submitted password must:
  * be at least 8 characters in length
  * contain at least one upper case letter
  * contain at least one lower case letter
  * contain at least one number
  * not contain any spaces
  If any of the above conditions are not met, the request should be rejected
  with a 400 status code and appropriate message.

  Upon successful registration of an administrator, an `Info` log entry should
  be made indicating that a new administrator was added and include the 
  username.  If an unsuccessful registration attempt is made, a `Critical`
  log entry should be made indicating that an unsuccessful attempt was made
  and the message should describe the specific reason why the attempt was 
  unsuccessful (i.e., which of the criteria above was violated)

* `POST /admin/all_attendings` retrieves a list of all attending physicians
  and their respective patients.  This route receives a JSON input as follows:
    ```
      {
          "admin_username": <username>,
          "admin_password": <password>
      }
    ```
  where
  * `<username>` is a string containing the username of the new administrator
  * `<password>` is a string containing the password of the new administrator
  
  This route should check the submitted `<username>` and `<password>` against
  previously registered administrator data.  If there is a match, this route
  should return a list of dictionaries where each dictionary contains the 
  following information about an individual attending physician.
    ```
      {
          "attending_email": <attending_email>
          "patients": <list_of_mrns>
      }
    ```
  where
  * `<attending_email>` is a string containing the e-mail address of the 
  attending physician
  * `<list_of_mrns>` is a list of integers where each integer is the medical
  record number of a patient of the attending physician

  If the submitted username and password do not match previously registered
  administrator information, a "401 Unauthorized" server status code should
  be returned with an appropriate message.

* `POST /admin/all_abnormal_results` retrieves information about all of the
  abnormal results in the database.  This route receives a JSON input as 
  follows:
    ```
      {
          "admin_username": <username>,
          "admin_password": <password>
      }
    ```
  where
  * `<username>` is a string containing the username of the new administrator
  * `<password>` is a string containing the password of the new administrator
  
  This route should check the submitted `<username>` and `<password>` against
  previously registered administrator data.  If there is a match, this route
  should return a list of dictionaries where each dictionary contains the 
  following information about an individual patient with an abnormal result
    ```
      {
          "patient_mrn": <medical_record_number>
          "abnormal_results": <list_of_dictionaries>
      }
    ```
  where
  * `<patient_mrn>` is an integer containing the medical record number of a 
  patient
  * `<list_of_dictionaries>` is a list of dictionaries where each dictionary
  contains information on a test that has an abnormal result for the given 
  patient.  This dictionary should look like:
    ```
      {
          "test_name": <test_name>,
          "result": <test_result>,
          "timestamp": <date_time_stamp>
      }
    ```
    where
    * `<test_name>` is a string containing one of the pre-defined test names
    * `<test_results>` is an `int` or `float` that contains the result for the
    abnormal test
    * `<date_time_stamp>` is a string with the date and time of the test result
    formatted as follows:  `2018-03-09 11:00:36`.

  If the submitted username and password do not match previously registered
  administrator information, a "401 Unauthorized" server status code should
  be returned with an appropriate message.

* `POST /admin/delay_total` retrieves information about the total delay in
  responding to requests for each type of test.   This route receives a JSON 
  input as follows:
    ```
      {
          "admin_username": <username>,
          "admin_password": <password>
      }
    ```
  where
  * `<username>` is a string containing the username of the new administrator
  * `<password>` is a string containing the password of the new administrator
  
  This route should check the submitted `<username>` and `<password>` against
  previously registered administrator data.  If there is a match, it should
  return a dictionary.  The keys of the dictionary should be the pre-defined 
  test names.  The values for each key should a string that shows the total 
  elapsed time, in the format `HH:MM:SS`,
  between the current time and the requested time for each open request for 
  that specific test across all patients.  

  For example, assume there are three open requests in the database as such:
  * "TSH" from 3/1/2023 09:00:25 for Patient 1
  * "TSH" from 3/1/2023 15:30:16 for Patient 2
  * "HDL" from 3/1/2023 16:45:58 for Patient 1
  
  And, assume that the current time is 3/1/2023 17:00:00.  The elapsed time
  since the first TSH request is 7 hours, 59 minutes, and 35 seconds.  The
  elapsed time since the second TSH request is 1 hour, 29 minutes, 44 seconds.
  The two of these elapsed times together is 9 hours, 29 minutes, and 19 seconds.
  The elapsed time for the one "HDL" test is 14 minutes and 2 seconds.  So, 
  the resulting dictionary would be:
  ```
    {
        "TSH": "09:29:19",
        "HDL": "00:14:02",
        "LDL": "00:00:00",
        "HR": "00:00:00"
    }
  ```
  
  If the submitted username and password do not match previously registered
  administrator information, a "401 Unauthorized" server status code should
  be returned with an appropriate message.
  
  