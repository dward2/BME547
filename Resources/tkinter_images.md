# Using Images in `tkinter`

To load an image into a `tkinter` interface, you set the image property
of a Label or Button.

```
root = tk.Tk()                                  # Creates main window
tk_image = tk.PhotoImage(file="tenor.gif")      # Creates an image object
my_img_label = ttk.Label(root, image=tk_image)  # assigns the image object to a label
my_img_label.grid(column=0, row=0)              # Places label on the grid of the main window
root.mainloop()
```
But, this will only work with GIF and PPM/PNM images (see [here](https://tkdocs.com/tutorial/fonts.html#images)).

For a wider range of functionality, use the [Pillow](https://pillow.readthedocs.io/en/stable/index.html) 
package, which is a fork of the Python Imaging Library (PIL).  Unlike `tkinter`,
the `Pillow` package needs to be installed in your `requirements.txt` file.
Then, it can be imported as follows:
```
from PIL import ImageTk, Image
```  
**Important:** Make sure that you use the above import line *AFTER* you import
`tkinter`.  `tkinter` also has an `Image` class and we don't want that to 
overwrite the `PIL` version.


First, load in the image into a PIL image object.
```
image_obj = Image.open("cloud3.jpg")
```
Next, convert that PIL image object into a Tk image object as follows:
```
tk_image = ImageTk.PhotoImage(image_obj)
```
Then, this `tk_image` object can be used in the label declaration similar to
the example above.  

See the `Pillow` documentation [here](https://pillow.readthedocs.io/en/stable/index.html)
 for more information on other
transformations you can do on the image objects, such as resizing or cropping.

### If images won't display when following the above:
There can be an issue when adding an image, particularly with multiple windows,
that the image will not display.  This can be caused by Python garbage
collection when procedures that define pictures are finished.  Please
see <http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm> for
more information.  In sum, add the following line after defining the Lable
that adds the `tk_image` to the label variable as such:
```python
my_image_label.image = tk_image
```

### Changing the image displayed
To change the image in a Label that already exists:
* First, create a new tk_image variable following one of the approaches above.
For example:  
  ```python
  new_img_obj = Image.open("new_image.jpg")
  new_tk_image = ImageTk.PhotoImage(new_img_obj)
  ```
* Update the image associated with the Label as follows:
  ```python
  my_image_label.image = new_tk_image  
  my_image_label.configure(image=new_tk_image)
  ```


## Displaying images from variables in `tkinter` interface
The steps above show how you can add an image directly from a file on the local
computer.  But, how can base64 string encoded images be displayed?  As 
discussed on the [image_toolbox.md](image_toolbox.md) page, in addition to 
images being stored in a file, we can store them in Python variables as either
a base64 encoded string or an ndarray.  (Note, there are many other ways 
variables can be stored in Python, but we are focussing on these two for this
class).  The code below demonstrates how you can convert images in these
forms into a format that can be shown in `tkinter` as part of a Label as
above.

### Loading an ndarray containing an image into a Tkinter label

```python
# Input:
#    img_ndarray:  variable containing an ndarray with image data

from PIL import Image, ImageTk

img_obj = Image.fromarray(img_ndarray)
tk_image = ImageTk.PhotoImage(img_obj)

# Output:
#    tk_image:  variable that can be assigned to the 'image' property of a
#                 tkinter Label or Button
```

### Loading a base64 string containing an encoded image into a Tkinter label
First, convert the base64 string into an ndarray using the appropriate
transformation from the [image_toolbox.md](image_toolbox.md).  Then, use the
code above to load that ndarray into the Label.
