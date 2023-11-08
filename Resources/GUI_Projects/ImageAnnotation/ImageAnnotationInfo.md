# Image Annotation

Instructions for using the `ImageLabel` custom widget found in the 
`image_label` module

## Intro
The `image_label` module creates a tkinter widget class called 
`ImageLabel`.  This widget will display an image loaded from a given filename.
This widget has a method to allow text to be added to the image.

## Import
To use the `image_label` module:
1. copy the `image_label.py` file into the same folder as your GUI code.  
2. In your virtual environment, install the `Pillow` package: 
`pip install Pillow`
3. Include the following import statement into your GUI code:

```python
from image_label import ImageLabel
```

## API

`ImageLabel(parent, **options)`
* Returns an `ImageLabel` instance which acts like a `ttk.Label` widget with
  some additional features
* Options:
  * `filename` - a string with the path to the filename of the image to
    display.  If not specified, a default image is shown as a place marker.
  * `width` - an integer indicating the desired display width of the image.
    The image will be resized with constant aspect ratio.  If not specified,
    the default width is either the width of the image loaded from `filename`
    or 500 pixels if no `filename` is given.

`ImageLabel.add_text(x, y, **options)`
* Adds text to the image at a specified position.
* Arguments:
  * `x` and `y` - floats between 0.0 and 1.0 (inclusive) indicating the
    fractional location from the upper left corner where the added text should
    be centered.  Coordinates of 0.5 and 0.5 would put the text in the center
    of the image.
* Required Option:
  * `text` - a string containing the text to be displayed
* Optional Options:
  * `size` - an integer containing the font size of the text to be displayed.
    Default is 12.
  * `color` - a string indicating the color of the text to be added.  Can be
    a standard color such as `"white"`, `"black"`, `"red"`, etc.  Default is
    `"white"`.

`ImageLabel.revert_last_addition()`
* Removes the last text added to the image

`ImageLabel.clear_all_text()`
* Removes all text added to the image

`ImageLabel.load_image(filename)`
* Loads an image from a file and displays it in the widget.
* The `filename` parameter is a string with the path to the image file to load

`ImageLabel.width()`
`ImageLabel.width(new_width)`
* When called without a parameter, returns the current width of the widget.
* When called with an integer parameter, sets a new width of the widget.
