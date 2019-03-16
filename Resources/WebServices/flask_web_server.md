# Web Server Development With `Flask`
`flask` is a Python package for small-scale web server development.

### Example
```
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_on():
    return "Ideal Weight Server is On"

if __name__ == '__main__':
    app.run()
```

What did the above do?

`from flask import Flask`  imports the `Flask` class from the `flask` package.

`app = Flask(__name__)`
creates an instance of the Flask class that will run the server.  It is supplied
with the name of the current running module.

`@app.route("/", methods=["GET"]) `
is a decorator that tells the Flask server to attach the following procedure
to the route given by the first parameter.  In this case, the route is simply
the `"/"` path.  This route is accessed using GET requests.

`def server_on():` is the function that will be run when the '"/"' path
is sent a request.  In this case, the function returns a string intended to
let the client know that the server is active.

`app.run()` starts the server.  

When the program is run, you will see something like the following in the
console:
```
FLASK_APP = iwc_server.py
FLASK_ENV = development
FLASK_DEBUG = 0
In folder C:/Users/dwonl/repos/WebServerLectures
C:\Users\dwonl\repos\WebServerLectures\venv\Scripts\python.exe -m flask run
 * Serving Flask app "iwc_server.py"
 * Environment: development
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
The server has started on your local computer and can be accessed through
the URL `http://127.0.0.1:5000`.  This is the standard IP address for 
accessing locally run servers, and can only be accessed from your computer.

To access the server, you could do one of two things:
1.  In a browser, visit `http://127.0.0.1:5000/`, or
2.  make a request such as follows:  
  ```
    import requests

    r = requests.get("http://127.0.0.1:5000/")
    print(r.text)
```
Next, lets add another route to our server.  First, we must import two
additional items from flask:
```
from flask import Flask, jsonify, request
```
Then, here is the function to add a second route to our server:
```
@app.route("/calculate_iwc", methods=["POST"])
def calculate_iwc():
    in_data = request.get_json()
    age = float(in_data["age"])
    gender = in_data["gender"]
    height = float(in_data["height_in"])

    ideal_weight_kg = 48.0 + 2.7 * (height - 60)
    ideal_weight_lb = ideal_weight_kg * 2.20462
    return jsonify({"input data": in_data, 
                    "ideal weight in lb": ideal_weight_lb})
```
The `@app.route` decorator defines that the URL path `/calculate_iwc` will
run the function below it called `calculate_iwc`.  Note that in this case,
the route name and function name are the same, but they do not have to be.
The decorator also defines that this route is accessed using POST requests.

Inside the function, the line `in_data = request.get_json()` uses the `flask`
object `request` to access the data accompanying the POST request.  In this
case, the JSON associated with the POST is copied into the variable `in_data`.
The remainder of the procedure calculates the ideal weight based on the given
input data.  

Finally, the `flask` function `jsonify()` is used to serialize the answer
into a JSON string for transmittal back to the client.  In this case, the
function defines a dictionary with the input variables and the result.