# Web Server Development with Flask
## Intro
In the previous lecture, we learned how to use the `requests` package in Python
to make GET and POST requests from our local computer (the client) to
a web server and receive and understand the response.

In this lecture, we will learn how to develop a server to receive GET and POST
requests and return a response.

## Flask
`flask` (<https://palletsprojects.com/p/flask/>) is a Python package that
allows us to create a web service/server that can expose a RESTful API.  It is
a lightweight framework for small scale web development.  `flask` gives the
developer functionality for creating a web service.  While we will be using
`flask` in this class, other packages are also
available to provide similar functionality, such as 
<a href = "https://www.djangoproject.com/">Django</a> and 
<a href = "https://www.tornadoweb.org/en/stable/">Tornado</a>.

### Steps To Create a Web Server with Flask
* Install `flask` in your virtual environment
* See <a href="../Resources/WebServices/flask_web_server.md">Resources/WebServices/flask_web_server.md</a>
for detailed example of writing `flask` code for a web server.  

### Learning Objectives
* Create a server with two GET endpoints and run locally.
  + Describe use of:
    + `from flask import Flask, jsonify, request`
    + `app = Flask(__name__)`
    + `app.route("/", methods=["GET"])`
    + `app.route("/info", methods=["GET"])`
    + `return` returns a string as a response
    + `return jsonify(python variable)` is needed to convert non-string
       variables into a JSON string for return
       - Note that `jsonify` must be used with the `return` statement.  It will
         not function properly if done on its own.  
         Example that will not work:
         ```
            x = jsonify(result)
            return x
         ```
         Example that will work:
         ```
            return jsonify(result)
         ``` 
    + `app.run()` in `if __name__ == "__main__":` code
* Access these endpoints by browser and local client program.
  + Describe `localhost:5000` and `http://127.0.0.1:5000`
  + Show how server can run in one terminal window while client in a second
    terminal window
* Add a POST endpoint to the server.  Receive a JSON
  + `app.route("/calculate", methods=["POST"])`
  + `in_data = request.get_json()`
* Add a variable URL
  + `@app.route("/sayhello/<name>", methods=["GET"])`
  + `def say_hello(name):`

    
<!---### As Time Allows
* Run external server
  + `app.run(host="0.0.0.0")`
* Demonstrate in PyCharm
* Run python vs Run flask (FLASK_APP=my_server.py flask run --host=0.0.0.0)--->