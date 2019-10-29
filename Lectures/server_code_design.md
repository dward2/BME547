# Server Code Design

### Modularity and Data Validation
* Flask handler functions (those decorated with `@app.route`) should only:
  + Receive data from the route request
  + Call other functions which validate inputs and complete tasks
  + Return information to requestor
* Data validation should include that the input JSON has the appropriate 
information (correct keys if a dictionary, correct data types, appropriate 
input as given by API specifications).
* If the input data is not correct, the flask handler should return the
appropriate [status code](https://www.ietf.org/assignments/http-status-codes/http-status-codes.xml).
* Status codes can be returned as follows:  
`return jsonify(message_or_other_info), status_code`  
where `status_code` is the integer value of the status code number.  If no
`status_code` is given, it is assumed to be `200`.
* Have any code needed to run upon the start of the server (e.g., logging
set-up, database creation) be done in one or more functions that can be called
from an init() function called from `if __name__ == "__main__":`.



  

