# Step-By-Step Workings of Server-Client Communication in Python
This page will go step by step through a simple server-client interaction 
between [server code](iwc_server.py) and [client code](iwc_client.py).

The code would be run in a virtual environment 
that has the `flask` and `requests` packages installed.

## Starting the Server
The [server code](iwc_server.py) is in the file `iwc_server.py`.  Based on how 
the code is 
written, there are two ways to start the server.  We are going to discuss the
first method initially, which is to simply run the code (by using your IDE or 
from the command line by entering `python iwc_server.py`).

The python interpreter will then start going through the code file.  The text
below will go through the code line by line as if it were being inspected by
the interpreter, along with an explanation of what the code does.

As always, the interpreter starts at the top of the file, ignoring any
commented lines. 

```
from flask import Flask, jsonify, request
```  
The necessary classes and functions from the `flask` package are imported.
Their specific functions will be discussed below as they are encountered.
```
app = Flask(__name__)
```
An instance of the `Flask` class is created and stored in the `app` variable.
This class is sent `__name__`, the name of the file being called, so it knows
what code is associated with the server.  This class stored in `app` handles
all of the server functions for receiving requests from the network and
providing responses.  For this
class, all you need to know is that this line must be at the top of your code
so it can be globally accessible.  If you want to know more about it, 
you can always check the documentation to learn more.

```
@app.route("/", methods=["GET"])
def server_on():
```  
The interpreter comes across a decoration called `@app.route`.  This tells the 
interpreter that the function following the decorator should be called when a 
request is made to the server at the `/` route (hence the decorator name
`@app.route` meaning to assign a route to the server defined in `app`).  
For now, the interpreter and server stores 
that fact away, that "/" would call the `server_on()` function.

It then continues until it finds the next decorator / function pair:
```
@app.route("/info", methods=["GET"])
def information():
```
Again, the interpreter stores away that a web request to `/info` route should
run the function `information()`.

Again, the interpreter continues down the file.
```
@app.route("/calculate_iwc", methods=["POST"])
def calculate_iwc_request():
```
Again, the interpreter stores away that a web request to `/calculate_iwc` route 
should
run the function `calculate_iwc_requests()`, and continues looking at the file.

```
def calculate_iwc(gender, height):
```
Here, the interpreter comes across a function without a decorator.  It
simply notes that this function exists, but does not tie it to any route
or server call.

```
if __name__ == '__main__':
    app.run()
```
The interpreter then reaches our familiar entry point.  It sees this `if` 
statement, and runs the code in the `if` statement.  The `app.run()` command
is telling our Flask class instance of `app` to `run` the server function. 

With this command, we will see our first output in the console:
```
CONSOLE OUTPUT:
D:\ClassRepos\WebServerLectures\venv\Scripts\python.exe D:/ClassRepos/WebServerLectures/iwc_server.py
 * Serving Flask app "iwc_server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
This message is telling us that the server has started and it can be reached
at `http://127.0.0.1:5000`.  At this point, the server code is simply waiting
to receive a request to that server.  It will keep doing that until the
server is shut off by pressing Ctrl+C (or terminating the process in your IDE).

#### Alternate Server Start Method
As mentioned above, there is a second way to start the server.  Instead of
running the code and getting the server started by using the `app.run()`
statement, you can tell `flask` to start the server from the command line
as follows:
```
FLASK_APP=iwc_server.py flask run
```
The `FLASK_API=iwc_server.py` command tells `flask` where the server code
can be found.  Then `flask run` tells flask to run the server.  If you use
this approach, you do not need the `if __name__ == "__main__":` portion of
the code.

## Client Code
Now that the server is running, the client program can be started which will
access the code.  The [client code](iwc_client.py) is in the file 
`iwc_client.py`.  For this
demonstration, it is written in a script format.  For most applications, it
would be better to be written in typical functional format.

The text below will go through the client code line by line as would be done
by the interpreter.

```
import requests
``` 
The interpreter will import the `requests` package that provides functionality
for making web server requests and receiving the results of those requests.  

```
# Check to see if server is on
print("Checking if server is on by accessing '/' route")
r = requests.get("http://127.0.0.1:5000/")
```
In this section of code, first a line is printed to the console communicating
what is happening in the code.

On the next line, the `requests.get()` function from the `requests` package
is called.  This makes a GET request to the given URL contained in the string
given as an argument.
A GET request is typically asking for information from a server.  The given
URL is `http://127.0.0.1:5000/`.  The server address itself is 
`http://127.0.0.1:5000` and the route being called is `/`.  This GET request
is sent to the internet by the `requests` package.

## Back to the Server:  Receiving GET request to `/`
The GET request above is received by the specified
server, which is running and listening for requests.  The server sees a GET
request to the `/` route.  The server has associated with `/` route with the
`server_on()` function, and so will run the following function:
```
@app.route("/", methods=["GET"])
def server_on():
    return "Ideal Weight Server is On"
```
The server will accept this request because it is a GET request, and the 
`@app.route` decorator has set the methods to "GET".  The function 
returns a string.  In general, most web communication is done in strings.
So, the server will send whatever is returned by the function as a string
back to the calling client.  And, then the server will wait for its next 
request.

## Back to the Client: Receiving Response from Server
The client code picks back up at the following line.
```
r = requests.get("http://127.0.0.1:5000/")
```
The response to the GET request is received by the client and put into the 
`r` variable.  This `r` variable now contains an object defined by the 
`requests` package that contains information about the response.

```
print("'r' type is {}".format(type(r)))
print("'r' = {}".format(r))

CONSOLE OUTPUT:  
'r' type is <class 'requests.models.Response'>
'r' = <Response [200]>
```
The `type` of `r` is printed as `<class 'requests.models.Response'>`
When the `r` variable itself is printed, it shows the response code received 
from the
server.  Here, the 200 response code says that the request was successful.

```
print("'r.text' = {}".format(r.text))
print("'r.text' type is {}".format(type(r.text)))

CONSOLE OUTPUT:  
'r.text' type is <class 'str'>
'r.text' = Ideal Weight Server is On
```
The `.text` attribute of the `r` variable contains the text string that was
returned by the server.  As you can see from the output, `r.text` is a `str` or
string and contains
the exact string that was returned by the server function `server_on()`.

Note that if the code tried to access the `r.json()` function, the code
would have created an error.  This is because the string that was returned
by the server is not in JSON format, and so the `r.json()` function would
not know what to do and generate an error.

The client then goes onto the next set of commands:
```
# Get information from server
print("Making a GET request to '/info' route")
r = requests.get("http://127.0.0.1:5000/info")
```
Another GET request is made to the same server, but this time, the `/info`
route is specified.  The GET requests goes out to the server.

## Back to Server:  Receiving GET request to `/info`
The above GET request is received by the server.  The server knows that the
`/info` route should be handled by the associated function:
```
@app.route("/info", methods=["GET"])
def information():
    info_string = "Information about server"
    calc_info_string = "Information about calculation"
    out_dictionary = {"info": info_string, "calc_info": calc_info_string}
    return jsonify(out_dictionary)
```
The GET request to `/info` is accepted as the method `"GET"` is specified
in the `@app.route` decorator.  The `information()` function is called.
It generated two strings, and then creates a dictionary using those two 
strings.  As discussed on the [flask_web_server.md](https://github.com/dward2/BME547/blob/main/Resources/WebServices/flask_web_server.md#jsonify-usage-notes)
page, data transfer over the web is generally done by strings.  So, the server
needs to encode the dictionary into a JSON string.  While Flask will
automatically do this for a dictionary, in this code the use of the `jsonify()` 
function imported from the `flask` package does it explicitly.  The line 
```
    return jsonfify(out_dictionary)
``` 
takes
the Python dictionary in `out_dictionary` and turns it into a JSON-formatted
string, when is then returned by the function.  This sends this JSON-formatted
string out into the internet, back to the client.

## Back to Client:  Receiving response from server
The client code had left off at
```
r = requests.get("http://127.0.0.1:5000/info")
```
The response from the server is stored in the `r` variable.
```
print("'r' type is {}".format(type(r)))
print("'r' = {}".format(r))

CONSOLE OUTPUT:  
'r' type is <class 'requests.models.Response'>
'r' = <Response [200]>
```
Printing `r` gives the response code, that in this case says there was a 
successful request.

```
print("'r.text' type is {}".format(type(r.text)))
print("'r.text' = {}".format(r.text))

CONSOLE OUTPUT:  
'r.text' type is <class 'str'>
'r.text' = {"calc_info":"Information about calculation",
            "info":"Information about server"}
```
`r.text`, the text attribute of variable `r`, is the string that was returned
by the web server.  This string is formatted as a JSON, so it can be imported
into a Python data structure, as done in the next lines.

```
print("'r.json()' type is {}".format(type(r.json())))
print("'r.json() = {}'".format(r.json()))

CONSOLE OUTPUT:
'r.json()' type is <class 'dict'>
'r.json() = {'calc_info': 'Information about calculation', 'info': 'Information about server'}'
```
`r.json()` takes the JSON string that was returned by the web server and 
deserializes or decodes it into a Python data structure, usually a dictionary.
The type of `r.json` is reported as a `dict`.

Next, the client code runs the following:
```
# Ask server to calculate ideal weight
print("Asking server to calculate ideal weight")
patient_data = {
                "age": 43,
                "height_in":  52,
                "gender": "female"
               }
r = requests.post("http://127.0.0.1:5000/calculate_iwc", json=patient_data)
```
This time, a POST request is being made.  A POST request sends information
to the server and awaits a response.  The POST request is made using the 
`requests.post()` function.  It has two arguments.  The first is the URL
of the server and route to be called.  The second is the information to be 
sent to the server.  As discussed above, this information must be sent as a
string.  But, the client has the information in a dictionary.  So, the 
dictionary must be converted to a JSON string to be sent over the internet.
This is done by using the `json=` argument in the `requests.post()`
argument list.  So, the JSON string is went with the POST request to the
server.

## Back to Server:  Receiving POST request to `/calculate_iwc`
The waiting server now receives this POST request to the `/calculate_iwc` 
route.  The server finds the code associated with this route:
```
@app.route("/calculate_iwc", methods=["POST"])
def calculate_iwc_request():
    in_data = request.get_json()
    age = float(in_data["age"])
    gender = in_data["gender"]
    height = float(in_data["height_in"])

    ideal_weight = calculate_iwc(gender, height)

    return jsonify({"input data": in_data,
                    "ideal weight in lb": ideal_weight})
```
This POST request is accepted as the `@app.route` decorator is set to the 
POST method.  
The function `calculate_iwc_request()` is run on the server.  This procedure
needs a dictionary containing the information needed for the calculation.
This dictionary is contained in the JSON string that was sent with the POST
request.  To access this JSON string and convert it to a Python dictionary,
the function `request.get_json()` is used.  It decodes the JSON string and
puts the results into the variable `in_data`.  Once this dictionary is
created, the needed information can be extracted from the dictionary and
then sent to a separate procedure, `calculate_iwc`, to do the calculations.

Note that the actual calculations are done in a separate function.  This is
for testing purposes.  The function associated with an `@app.route` decorator
is hard to test as it requires internet calls to receive and send information.
So, all calculations should be done in a separate function that can be
tested, and the function associated with the `@app.route` decorator should
only handle data input from the server request and returning the appropriate
answer.

Once this function has the answer (in this case, the `ideal_weight`), it 
then returns the answer in a JSON format using `jsonify`.

## Back to Client
The client left off here:
```
r = requests.post("http://127.0.0.1:5000/calculate_iwc", json=patient_data)
print("'r' = {}".format(r))
print("'r.json() = {}'".format(r.json()))

CONSOLE OUTPUT:
r' = <Response [200]>
'r.json() = {'ideal weight in lb': 61.5, 
             'input data': {'age': 43, 'gender': 'female', 'height_in': 52}}
```
As previously, the information returned from the POST request is put in the
`r` variable, and is imported into a Python dictionary using the `r.json()`
function.  