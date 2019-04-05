# Using Images in `tkinter`

To load an image into a `tkinter` interface, you set the image property
of a Label or Button.

```
root = Tk()  # Creates main window
my_image = PhotoImage(file="tenor.gif")  # Creates an image object
my_img_label = Label(root, image=my_image)  # assigns the image object to a label
my_img_label.grid(column=0, row=0)  # Places label on the grid of the main window
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
First, load in the image into a PIL image object.
```
image_obj = Image.open("cloud3.jpg")
```
Next, convert that PIL image object into a Tk image object as follows:
```
my_image = ImageTk.PhotoImage(image_obj)
```
Then, this `my_image` object can be used in the label declaration similar to
the example above.  

See the `Pillow` documentation [here](https://pillow.readthedocs.io/en/stable/index.html)
 for more information on other
transformations you can do on the image objects, such as resizing or cropping.

