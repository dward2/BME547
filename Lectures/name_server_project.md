# Mini-Projects

## Name Server
Write a program that uses the `request` library to POST student
data to a server at `http://vcm-6764.vm.duke.edu:5000`.  And, use a
POST to the same server ti get the results of adding two numbers.

For syntax help, see [this Jupyter Notebook](/Resources/WebServices/requests.ipynb).

The server has the following endpoints:

* `POST http://vcm-6764.vm.duke.edu:5000/student`  
allows you to add your
student data.  The associated POST data should look like this JSON:  
    ```
    {
       "name": "David Ward",
       "net_id": "daw74",
       "e-mail": "david.a.ward@duke.edu"
    }
    ```  
  If successful, the POST request will return a JSON with a "message" key and a
"number of students" key.  If the request is unsucessful, it will return a
JSON with a string giving the reason.

* `GET http://vcm-6764.vm.duke.edu:5000/list`  
returns a list of all the student data currently available on server

* `POST http://vcm-6764.vm.duke.edu:5000/sum`  
allows you to compute a standard sum based on JSON input that looks like:
  ```
  {
     "a": 1,
     "b": 2
  }
  ```

## Blood Match
A blood type matching server is running at URL `http://vcm-10183.vm.duke.edu:5000`.

Write a program the completes the following tasks:

* Get the IDs for two patients by making a GET request to `URL/get_patients/<name>`.  
Replace `<name>` with your Duke Net ID.  
This request will return a dictionary
in the following format:  
`{"Recipient": "<ID1>", "Donor": "<ID2>"}`.
* Obtain the blood type of the two patients by making GET requests to 
`URL/get_blood_type/<id>` where `<id>` is replaced by either `<ID1>` or `<ID2>`
from above.  
This request will return a string with the blood type of the given patient.
* Calculate whether it is an acceptable match for the recipient to receive
blood from the donor.
* Check your result by making a POST request to `URL/match_check`.  Send a
JSON with the following format:  
`{"Name": "<name>", "Match":  "<answer>"}`  
Replace `<name>` with your Duke Net ID and `<answer>` with either `Yes` or `No`.  
This request will return "Correct" or "Incorrect".
