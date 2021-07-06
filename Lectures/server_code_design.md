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
  
## In-Class Project

Develop a health database server

### Routes
` POST /new_patient`

```python
{"name": str, "id": int, "blood_type": str}
```
where blood type is one of O+, O-, A+, A-, B+, B-, AB+, AB-.


`POST /add_test`

```python
{"id": int, "test_name": str, "test_result": int}
``` 

`GET /get_results/<patient_id>`


### Event-Driven Code
* Servers (and as we will discuss later, GUIs) are event-driven processes.
  Once the server is set up, it "waits" for some sort of event to determine
  what code to run next.  These "events" are GET or POST requests.  Since
  these events are generated external to the server, the server cannot 
  guarantee what order the events will occur.  So, the code cannot be written
  to assume that the events will happen in a certain order.  If they do need
  to happen in a certain order, the code needs to recoqnize when the order
  is violated and provide an error/feedback message indicating that the 
  correct order was not followed.  And, the server should not crash or cause
  problems when the incorrect order is followed.


  

