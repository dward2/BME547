## Heart Rate Sentinel Server Administrator Function

* `POST /api/new_administrator` that takes a JSON as follows:
    ```
    {
        "admin_username": <admin_username_as_str>,
        "admin_password:": <password_as_str>
    }
    ```
    This route is registering an administrator account with your server.  The
    administrator will have access to all of the data available on the server.  In
    the JSON above, `<admin_username_as_str>` should be replaced by a string 
    containing a user name and `<password_as_str>` should be replaced by a
    string containing a password.  
    
    The submitted username must not be an empty string.
    The submitted password must be 8 or more characters in length and include
    at least one letter and one number with no spaces.  If either of the above 
    conditions are not met, the request should
    be rejected with an appropriate message and status code.
      
* `POST /api/admin/all_attendings` that takes a JSON as follows:
    ```
    {
        "admin_username": <admin_username_as_str>,
        "admin_password:": <password_as_str>
    }
    ```
    This route will check the submitted `<admin_username_as_str>` and 
    `<password_as_str>` against previously registered administrator data.  If 
    there is a match, this route should return a list of attending physician
    information.  This list should be a list of dictionaries that look like this:
    ```
      {
          "attending_username": "Smith.J",
          "attending_email": "dr_user_id@yourdomain.com", 
          "attending_phone": "919-867-5309"
      }
     ```
    If the submitted username and password does not match previously registered
    administrator information, a "401 Unauthorized" server status code should
    be returned with an appropriate message.
    
* `POST /api/admin/all_patients` that takes a JSON as follows:
    ```
    {
        "admin_username": <admin_username_as_str>,
        "admin_password:": <password_as_str>
    }
    ```
    This route will check the submitted `<admin_username_as_str>` and 
    `<password_as_str>` against previously registered administrator data.  If 
    there is a match, this route should return a list of patient
    information.  This list should be a list of dictionaries that look like this:
    ```
      {
          "patient_id": 1, # usually this would be the patient MRN
          "attending_username": "Smith.J", 
          "patient_age": 50, # in years
      }
    ```
    If the submitted username and password does not match previously registered
    administrator information, a "401 Unauthorized" server status code should
    be returned with an appropriate message.

* `POST /api/admin/all_tachycardia` that takes a JSON as follows:
    ```
    {
        "admin_username": <admin_username_as_str>,
        "admin_password:": <password_as_str>,
        "since_time": "2018-03-09 11:00:36"
    }
    ```
    This route will check the submitted `<admin_username_as_str>` and 
    `<password_as_str>` against previously registered administrator data.  If 
    there is a match, this route should return a list of dictionaries where
    each dictionary represents a specific tachycardia incidence.  The route
    should examine all available heart rates for all patients.  If the posted
    heart rate is tachycardic, a dictionary should be added to the list in
    the following format:
    ```
      {
          "patient_id": 1,
          "attending_username": "Smith.J",
          "attending_email": "dr_user_id@yourdomain.com", 
          "tachycardia_datetime": 2018-03-09 11:00:36
      }
    ```
    If the submitted username and password does not match previously registered
    administrator information, a "401 Unauthorized" server status code should
    be returned with an appropriate message.