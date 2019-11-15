# Sending and Receiving Images/Files using Flask and Requests
### Sending Image with Requests
```
import requests

files = {'file': (<fn_string>, open(<fn_to_send>, 'rb'))}

r = requests.post(<URL>, files=files)
```
* `<fn_to_send>` is a string with the filename of the file you want to send.
* `<fn_string>` is a string that the server will receive indicating the name
to be associated with the file being sent.  `<fn_string>` does not need to 
match `<fn_to_send>` unless you want the server to use the exact same name as
the client.
* `<URL>` is the URL of the server route waiting to receive a file.


### Receiving Image with Flask
```
from flask import Flask, request

app = Flask(__name__)

@app.route("/receive_image", methods=["POST"])
def receive_image():
    f = request.files['file']
    f.save(f.filename)
    return "{} successfully saved".format(f.filename), 200
```
* In the code above, the `"/receive_image"` route name, the  `receive_image()`
function name, and `f` variable name can be any route or name as needed.
* The above example saves the file using the filename sent in the request. The
arguement in the `f.save()` function can be any string desired.

### Links
* Flask Uploading Files: <https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/#uploading-files>
* Requests, Posting a File:  <https://requests.kennethreitz.org/en/master/user/quickstart/#post-a-multipart-encoded-file>

### Storing Image in MongoDB
Images can be stored in MongoDB, using PyMODM, in two ways.
1.  Convert the image to a base64 string (see 
[image_encoding_decoding.md](../Lectures/image_encoding_decoding.md)) and store in a
`CharField()`, or
2.  Convert the image to a base64 encoded bytes and store in a `BinaryField()` 