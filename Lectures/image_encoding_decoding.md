# Image Encoding / Decoding

## Images
At the most basic level, a digital image is a series of bits (0s and 1s).
How those bits are translated into the visual image is dependent on the 
format of the image file.  Formats include JPG, GIF, TIFF, PNG, BMP, etc.

In general, formats include information such as:
  * Are pixels stored by rows or by columns
  * Bit depth, or how many bits are required to define each pixel
    + Greyscale:  each pixel has a base10 value of 0 to 255 (8 bits)
    + Color:  each pixel has values for Red, Green, Blue, each of 0 to 255, or
    24 bits
  * Additional compression of the data
  
But, whatever format is used, the image is represented by a series of binary 
numbers.

## Encoding / Decoding
Encoding is taking a data format and changing it into some other
format that is more readily shared with other programs or across the web.

For example, we have been using JSON encoding to take native Python data 
structures such as lists and dictionaries and "encoding" them into JSON strings 
that can be sent over the internet and interpreted by other programs.

Decoding is simply the reverse.

### Encoding binary data
In the binary (base2) system, I have two symbols for representing numbers.
Take the binary (base 2) number 101011.  If this translated directly into a
string for sending over the web, it would be "101011".  This is 6 characters
long.

__base10__

base10, of course, uses ten symbols (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) to
represent numbers.  If we "encode" this binary number 101011 into the base10 
system, its value is "43".  As a string, this would be only two characters 
long, and hence shorter to transmit.

__base16__

base16 adds 6 additional symbols (a, b, c, d, e, f) for representing numbers.
The binary number 101011 translates to "2b" in base16, also known as 
hexadecimal.

__base64__
 
The [base64](https://en.wikipedia.org/wiki/Base64#Base64_table) system uses
64 characters to represent numbers.  These symbols include upper case letters,
lower case letters, numbers, and various punctuation.  The binary number 101011 
translates to "r".  

As we increase the number of characters or symbols used to represent numbers,
the number of characters needed to represent a particular number decreases.  
When sending as a string over the web, smaller is better.

## Encoding an image 
The binary number series of an image can be converted into a base64 string for
transmission over the internet and/or for storage as a string in a database 
such as MongoDB.  Python has a built-in module called `base64` that contains
encoding and decoding functions for base64.  It is a built-in
module, and so while it needs an `import base64` in the code, it does not need 
to be separately installed in a virtual environment.

Below is sample code for using `base64` for encoding and decoding an image.

```
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


def read_file_as_b64(image_path):
    with open(image_path, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


def view_b64_image(base64_string):
    image_bytes = base64.b64decode(base64_string)
    image_buf = io.BytesIO(image_bytes)
    i = mpimg.imread(image_buf, format='JPG')
    plt.imshow(i, interpolation='nearest')
    plt.show()
    return
    
    
def save_b64_image(base64_string):
    image_bytes = base64.b64decode(base64_string)
    with open("new-img.jpg", "wb") as out_file:
        out_file.write(image_bytes)
    return


if __name__ == '__main__':
    img_b64_string = read_file_as_b64("D:\dwonl\Pictures\Sight.jpg")
    view_b64_image(img_b64_string)
    save_b64_image(b64_string)
```
The file encoding is demonstrated in the `read_file_as_b64()` function.  
  * First,a binary image file is opened using the `image_file` variable.
  * `image_file.read()` reads in the binary bytes from the image file.
  * `base64.b64encode` takes the bytes from the image file and encodes them
  into base64 encoded bytes, saved in the `b64_bytes` variable.
  * As a `bytes` object is not JSON-serializable, the `b64_bytes` is converted
  to a `str` type using the `str()` command.  The string encoding method of
  `utf-8` is used.  (Note: an alternate method is 
  `b64_string = b64_bytes.decode()` which decodes the bytes into a string.)
  
The base64 string could now be sent to or returned by a web server as a JSON.

The base64 string can then be decoded, as demonstrated by the `view_b64_image()`
function.
  * The `base_64_string` received as an argument is decoded using 
  `base64.b64decode()`.  It saves the resulting bytes in a variable 
  `image_bytes`.
  * In this example, instead of saving these bytes to a file on disk, they are
  put into an IO stream using the `io.BytesIO()` function.  This function takes
  the bytes and converts them into an IO stream in memory that acts like a 
  file.  This IO stream is referenced by the `image_buf` variable.
  * The image from the `image_buf` is read in by the `matplotlib` function
  `mpimg.imread`.  The expected format of the image is given so the image
  interpreter will understand the format of the bytes.
  * Finally, `plt.imshow()` and `plt.show()` are used to display the image.

The process for saving the base64 string into an image file on disk is
demonstrated by the `save_b64_image()` function.
  * The base64 decoding is done the same as in the `view_b64_image()` function.
  * The resulting bytes are then written to a binary file. 
  
## Image Toolbox
On the page [image_toolbox.md](../Resources/image_toolbox.md) in the Resources
section, I describe in more detail the various transformations and states that
the image data can be held in Python, including the base64 encoding and
decoding.  Also included is code to perform the various transformation.  This
information provides a basis for using and manipulating images for your final
project. 

## Documentation Links
* <https://docs.python.org/3/library/base64.html>

## Image Server API for In-Class Work
### Server API

URL is `http://vcm-21170.vm.duke.edu`.  (Port is 80, so not needed in URL)

### POST `/add_image`
Add an image to the database and display on webpage.  _Please upload only JPG
files._

Requires the following dictionary as JSON string
```python
{"image": <base_64_string>, "net_id": <net_id>, "id_no", <int>}
```
  + `<base_64_string>` is a string containing an image encoded into base 64
  + `<net_id>` is a string containing your Duke Net Id
  + `<int>` is an integer and will be used to tag the image for further retrieval

Returns `string` with message about the outcome of the Post.

### GET `/get_image/<net_id>/<id_no>`

Retrieves the stored image with a watermark added.

Variable URL where:
  + `<net_id>` is the Duke Net Id used to store the image as above
  + `<id_no>` is the integer used to tag the image as above

Returns `string` containing the image encoded as a base 64 string.

## In-Class Exercise
### Write client code that does the following:
1. Converts an image file to a base64 string (USE A JPG FILE)
   1. The filename can be hard coded or you can ask it from user using 
   `filedialog.askopenfilename()`
2. Uploads that base64 string to the server
3. Downloads a base64 string for the "watermarked" image
4. Saves the downloaded base64 string as an image file
   1. Download filename can be either hardcoded or you can ask it from user
   using `filedialog.asksaveasfilename()`

### If time, create a GUI that will display the downloaded file.
* Have the GUI automatically do steps 1 through 3 above
* Then, have it display the image in the GUI rather than save it
* Alternate:  Add a button to the GUI that allows the user to select the 
  image to upload rather than hardcoding it.
