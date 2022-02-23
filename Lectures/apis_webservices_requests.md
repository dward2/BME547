# APIs, Web Services, and Requests

## APIs
An __Application Programming Interface__ (API) provides instructions and/or an
interface for accessing the functionality of a program or package.

Physical Example:  Microwave

Package Example:  `scipy`  
<https://docs.scipy.org/doc/scipy/reference/#api-reference>

The API defines the functions that the user calls and interacts with, while
masking the complicated details behind the scene.  

The keystones of an API are __functions__.  

When designing an API, you need to consider:
* What functions need to be exposed to the user
* How to ensure API functions are flexible enough to be "stable" for 5 years
while allowing for updates.
* Platform independent

## Web Services
Modern software design almost always has some relationship to cloud computing.

Advantages to cloud computing:  
* Improved information sharing
* Access to enhanced computing power
* Increased data storage and access
* Platform independent (client-independent API).  The server functionality
can be called from multiple types of clients (iOS, Windows, Web Apps, devices,
etc.)

To be a modern software developer, must have an understanding of web services
and cloud computing.

## RESTful APIs:  Making requests on the web
RESTful APIs are APIs in the cloud and are how we interact with web servers.

REST stands for **RE**presentational **S**tate **T**ransfer.

Instead of installing and calling packages on our local computer, RESTful APIs 
allow us to call functionality in the cloud (on a server).

## Definitions
### URL
Calls to web services are done through URLs (uniform resource locator).

URLs can be thought of as a function name to access a particular functionality
of a server.

Example:  `http://vcm-7631-vm.duke.edu:5000/sum`
* `http` is the protocol for how the information is to be transferred
* `vcm-7631-vm-duke.edu` is the host or hostname, that acts as an address to 
know which server to contact on the web.
* `5000` is the port used to access the server.  For typical web page display,
this is omitted and a default port is used.
* `/sum` is the path (or sometimes called the route).  It references the 
specific functionality of the server with which you want to interact.

### Client
A client is anyone (in our case, a computer program on our local computer) that
wants to interact or share information with a web server or service.

### Web Server or Service
A web server or service is a program running on a separate machine (another
computer, a cloud computer, or a computer cluster).

### Requests
A client makes a "request" of the server in order to interact.

### Response
The server sends a "response" back to the client after a request.  This 
response is often encoded as a JSON string.  JSON strings are a standard
method for information interchange over the internet.

## Making a Request
To interact with a RESTful API of a web service, you make a "request" of it.
In this class, we will focus on two request types:
* __GET__ - generally used to get information from a server
* __POST__ - generally used to send information to a server and perhaps
receive some information in return.

There is a lot of overlap between these two types.

### GET Example

GitHub API:  (<https://docs.github.com/en/rest>)

Let's get a list of all of our branches from a repository.

<https://docs.github.com/en/rest/reference/branches>

`GET /repos/{owner}/{repo}/branches` from requests made to `api.github.com`

A Python package called `requests` (<https://requests.kennethreitz.org/en/master/>)
provides functionality for making requests to web servers.

`import requests` imports the `requests` package.  It must be installed in your
virtual environment.

`r = requests.get("https://api.github.com/repos/dward2/BME547/branches)`

The `requests.get()` function makes a get request to the URL given in the 
string parameter.  The response from the server is stored in the variable `r`.

The response `r` is a `requests.models.Response` object defined by the 
`requests` package.  It contains lots of information about the response.
Printing `r` will only show the response code from the server.

Response Codes:  <https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml#http-status-codes-1>

Other useful information in `r`:
* `r.status_code` returns the status code as a number
* `r.text` will return the entire string response
* `r.json()` will deserialize (or decode) the JSON text string into a Python
native variable type.  The contents of the response will vary depending on the
specific server request that was made.  

### POST Example

__Name Server__

The server has the following endpoints:

* `POST http://vcm-21170.vm.duke.edu:5000/student`  
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
"number of students" key.  If the request is unsuccessful, it will return a
JSON with a string giving the reason.

* `GET http://vcm-21170.vm.duke.edu:5000/list`  
returns a list of all the student data currently available on server


<!---
__Country Server__

API:  <a href = "../Resources/WebServices/country_server_api.md">API</a>

Let's compare the information on Spain and Sweden.  (Note: if this server does
not respond, it may be shut off.  See the link "API" link above for more
information on checking on server status and requesting activation.)

```
import requests

countries = {"one": "Spain", "two": "Sweden"}
r = requests.post("http://vcm-7631.vm.duke.edu:5000/compare", json=countries)
print(r.json())
```
--->
For additional information on the above, see 
<a href="../Resources/WebServices/requests.md">Resources/WebServices/requests.md</a>

Also, an interactive Jupyter notebook is available at
 <a href="../Resources/WebServices/requests.ipynb">Resources/WebServices/requests.ipynb</a>

## In-Class Activity: Messaging API

Find a partner in class and write some code to:
* Send a message to your partner
* Receive a message from your partner

URL To Server:  `http://vcm-21170.vm.duke.edu:5001`

### `POST /add_message`
Posts a message for a specific user.

Expects json input: `{"user": <user_name>, "message": <message_string>}`

where 
* `<user_name>` is a string containing the name of user for whom to post
a message
* `<message_string>` is a string containing the message for the user.

### `GET /get_messages/<user_name>`

Retrieves messages for the user indicated by `<user_name>`.

Returns a list of messages for the user.  If the user has never had
a message posted, a status code of 400 is returned.  If the user
exists, but has no active messages, an empty list is returned.

## <a href="name_server_project.md">**Class Exercise Link**</a>