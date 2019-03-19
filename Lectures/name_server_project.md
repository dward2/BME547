# In-class Mini-Project

Write a program that uses the `request` library to POST the following student
data to a server at `http://vm-7631.vm.duke.edu:5000`.  Next, use the `/sum`
POST to get the results of adding two numbers.

For syntax help, see [this Jupyter Notebook](/Resources/WebServices/requests.ipynb).

The server has the following endpoints:

* `POST http://vm-7631.vm.duke.edu:5000/student`  
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

* `GET http://vm-7631.vm.duke.edu:5000/list`  
returns a list of all the student data currently available on server

* `POST http://vm-7631.vm.duke.edu:5000/sum`  
allows you to compute a standard sum based on JSON input that looks like:
  ```
  {
     "a": 1,
     "b": 2
  }
  ```