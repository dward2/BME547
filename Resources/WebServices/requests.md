# Web Services, APIs, and Requests
## Introduction
Modern software design almost always has some relationship to cloud computing.
The ability for local software and applications to access the cloud allows
for improved information sharing, access to enhanced computing power, and 
increased data storage and access.

For example, in designing a medical device, we may want it to be portable,
affordable, and have a long battery life.  These criteria may make it difficult
to design a device with the computing power desired.  If the device can
access a more powerful device or server in the cloud, it can offload the 
heavy-duty computation and data storage needed for its functioning and still
be able to be lightweight (in both size and performance).

Therefore, we need to learn how to make interact with web services with our
software and how to design those web services.

## APIs
An Application Programming Interface (API) provides instructions or an 
interface for accessing the functionality of a program or package.  

Let's think of a physical example.  Assume you have a toaster.  How does the
toaster actually work?  It takes electricity, sends it through a resistive
heating element at a certain voltage for a certain time.  A timer eventually
turns off the heat, generates some sort of signal, and maybe even eject the 
toast.  When you use a toaster, you don't specifically set current levels or
turn on the element, or monitor temperatures.  You simply press some buttons.
The buttons you press (on/off, toast darkness, timer) could be thought of
as the API that allows the user to access the functionality of the toaster.

Let's think about the packages you have used so far in this class.  Take
the `scipy` package.  There is lots of code in it to do all kinds of
calculations:  for example, the peak finding routines you may have used
for the ECG Analysis assignment (`scipy.signal.find_peaks`).  This function
call allows you to access some of the calculation methods within `scipy`.  The
`find_peaks` function is part of the API for `scipy`.  

For programming, APIs can be thought of as the functions of a package or
program that users can use.  In the `scipy` example, a user can go to the 
API Reference (<https://docs.scipy.org/doc/scipy/reference/#api-reference>) for
`scipy` and find all of the functions that can be used.  `find_peaks` can
be found at <https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html#scipy.signal.find_peaks>

APIs are also useful to provide a consistent interface to a program's 
functionality that won't change over time as the program grows/updates/changes
or is implemented on different platforms (PC/macOS/Android).

Your challenge as a developer:  to design an API for your software/services
that is user-friendly and will be stable over a period of years.

## RESTful APIs:  Making requests on the web
RESTful APIs are API's in the cloud and are how we interact with web servers.
Instead of importing or accessing functionality on our local computer,
RESTful APIs allow us to call functionality in the cloud.  They provide a 
standard convention for web service interface design.

REST stands for **RE**presentational **S**tate **T**ransfer.  (Provided for
your info only.  For more details, visit <https://resfulapi.net>.) 

Before we dive into using RESTful APIs for interacting with web servers, let's
review some terms.

### Definitions
#### URL
Calls to webservices are done through URLs, which can be though of as a 
function name to access a particular functionality of a server.

URL is a uniform resource locator.  An example of a URL is:

`http://vcm-7631.vm.duke.edu:5000/sum`

* `http` is the protocol for how the information is to be transferred
* `vcm-7631-vm.duke.edu` is the host or hostname, which acts as an address to
know which server to interact with.
* `5000` is the port used to access the server.  Depending on the web server,
it is often omitted.
* `/sum` is the path (or sometimes called the route).  It references the
specific functionality of the server you want to interact with.

Here is an easy to read website that explains more about URLs:  
<https://doepud.co.uk/blog/anatomy-of-a-url>

#### Client
A client is anyone (in our case, a computer program on our local computer) that
wants to interact or share information with a web server or service.

#### Web Server or Service
A web server or service is a program running on a separate machine (another
computer, a cloud computer, or a computer cluster)

#### Requests
A client makes a "request" of the server in order to interact. 

#### Response
The server sends a "response" back to the client after a request.  The response
is often encoded as a JSON string.  JSON strings are a standard method for
information interchange over the internet.

### Requests
To interact with a RESTful API of a web service, you make a "request" of it. 
In this class, we will focus on two request types:
* **GET** - generally used to get information from a server
* **POST** - generally used to send some information to a server, and perhaps 
receive some information in return

Note that there is overlap between the two types of requests.  For example,
with a GET request, we often need to send some information to the server so
the server knows what to send back to us.  

#### Example of GET Request
Let's look at GitHub's API (<https://developer.github.com/v3/>), specifically
at the GET request for the list of branches in a repository:
<https://developer.github.com/v3/repos/branches/#list-branches>

The API says that the call for a list of branches is defined as:
`GET /repos/:owner/:repo/branches` and that requests are made to the 
`api.github.com` host.  How do we make this request.

There is a Python package called `requests` (<https://requests.kennethreitz.org/en/master/>)
that gives us the ability to make requests to web servers.  The following
code block shows how it is done:

```python
import requests

r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
print(r)
answer = r.json()
print(answer)
for branch in answer:
    print(branch["name"])
```

First, we import the package with `import requests`.

Then, we make a web request by using the `requests.get()` function.  This
function takes as an argument the URL to which the request should be made.
Any response from the server is then stored in the variable `r`.

The response `r` is an `requests.models.Response` object defined by the 
`requests` package.  It contains lots of information about the response from
the server.  The statement `print(r)` will give the response code from the
server:
```
print(r)
Output:  <Response [200]>
```
This gives the web response status code.  A list of codes can be found at
<https://www.ietf.org/assignments/http-status-codes/http-status-codes.xml>.
The 200 code says the request was successfully run.

Other useful information that can be found in the response `r`.  
* `r.status_code` will return the status code as a number
* `r.text` will return the entire string response
* `r.json()` will deserialize (or decode) the JSON text string into a Python
native variable format.  The contents of this dictionary will depend on the
specific server request that was made.

For the `branches` request made to GitHub above, it will return a list of 
dictionaries, with each dictionary containing information about each branch
in the specified repository.  The example above iterates through each item
in the list and prints the value for the key "name" for each branch.

Try the sample code above for one of your own repositories.  Simply replace
the GitHub user id (`dward2`) and the repo name (`BME547`) with your own.

#### Example of POST Request
 ```
import requests

countries = {"one": "Spain", "two": "Sweden"}
r = requests.post("http://vcm-7631.vm.duke.edu:5000/compare", json=countries)
print(r.json())

Output:
name        Spain                 Sweden              
  pop.        40397842              9016596              
  area        504782                449964               
  gdp         22000                 26800                
  literacy    97.9                  99      

```
In the example above, `requests.post` is used to make a POST request to the
server found at hostname `vcm-7631.vm.duke.edu`.  (Note: this is a Duke VCM
which may not be turned on when you try this).  This server requires the 
addition of the `:5000` port to the hostname.  The specific functionality
requested is the `/compare` path.  This function requires a dictionary
with the two countries to be compared.  This dictionary is sent in the POST
request using the `json=` parameter.  By using this parameter, the Python
dictionary is serialized (or encoded) into a JSON string and sent over the 
internet to the server.  Again, the response from the server is stored in the
`r` variable.
  
## Next:  Writing a Server
Next, we will learn how to write code to power a server.




