# Image Handling Toolbox

## Intro
The code snippets below provide the code needed for handling images.  They 
assume that an image exists in one of three states:

* A file on your local computer
* A string of bytes encoded as a base64 string
* An ndarray containing the image data

When transferring data between client and server, use the base64 string as
strings are easily transmitted across the web.  (The base64 string can be part 
of a dictionary that is sent as a JSON in a POST request).  The base64
string can also be used to store the image in a database.    

To display the image in `matplotlib`, or to apply any of the scikit-image 
(`skimage`) functionality on the image, make sure the image is in the ndarray 
format.

The code blocks below provide code for converting between these different 
states.  

## Example

Let's diagram how an image would be transformed along the process of being
uploaded from a file on a local computer to a server for storage in a database, 
followed by transformation of the image and downloading of transformed image 
back to the local computer.

### Client
![client_upload.png](images/client_upload.png)
On the client-side, the image contained in a file is transformed into a base64
string.  This string is then sent to the server.

### Server
![server.png](images/server.png)
The server receives this base64 string and sends it to the database for 
storage.  The base64 string is then converted into an ndarray that contains
the image data.  This ndarray can be processed (inverted in this case) and
converted back to a base64 string and then sent back to the client.

### Client
![client_download.png](images/client_download.png)
The client receives the base64 string with the encoded processed image.  This
base64 string is converted to an ndarray for display using `matplotlib` and
is also converted into a file for storage on the computer.

The above workflow is accomplished by converting the image between the three
formats listed above, using the base64 string for communication and storage
in a database, using the ndarray format for image processing and display, and
the file format for storage on the local computer.  All of the needed
conversions are given in the code snippets below.

Note that there are other ways to send images across the web and for converting
and displaying images.  If you prefer to use those, feel free.  

## Toolbox Code

### Imports
These imports are need for the code blocks below.
```python
import base64
import io
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from skimage.io import imsave
```

### Convert image file to base64 string
```python
# Input:
#    filename: string variable containing the path and name of the image file 
#                on computer

with open(filename, "rb") as image_file:
    b64_bytes = base64.b64encode(image_file.read())
b64_string = str(b64_bytes, encoding='utf-8')

# Output:
#    b64_string: string variable containing the image bytes encoded as a base64 
#                  string
```

### Convert base64 string to image file
```python
# Input:
#    b64_string: string variable containing the image bytes encoded as a base64
#                  string

image_bytes = base64.b64decode(b64_string)
with open(new_filename, "wb") as out_file:
    out_file.write(image_bytes)

# Output:
#    an image file on the local computer with the path and name contained in
#      the new_filename variable
```

### Convert base64 string to ndarray containing image data
```python
# Input:
#    b64_string: string variable containing the image bytes encoded as a base64
#                  string

image_bytes = base64.b64decode(b64_string)
image_buf = io.BytesIO(image_bytes)
img_ndarray = mpimg.imread(image_buf, format='JPG')

# Output:
#    img_ndarray: variable containing an ndarray with image data
```

### Display image in ndarray format using `matplotlib`
```python
# Input:
#    img_ndarray: variable containing an ndarray with image data

plt.imshow(img_ndarray, interpolation='nearest')
plt.show()

# Output:
#    A `matplotlib` window with an image
```

### Convert image in ndarray format into a base64 string
```python
# Input:
#    img_ndarray:  variable containing an ndarray with image data

f = io.BytesIO()
imsave(f, img_ndarray, plugin='pil')
y = base64.b64encode(f.getvalue())
b64_string = str(y, encoding='utf-8')

# Output:
#    b64_string: string variable containing image bytes encoded as a base64
#                  string

```

