## Image Annotation
Write GUI code that allows a user to add text annotations to a medical image.
A custom widget called `ImageLabel` is provided that has functionality to
display an image and add text to it.

### Specifications
Design a GUI and associated program code that meets the following 
specifications.
* The GUI must display an image.
* The user must have the ability to input X and Y coordinates, in the range of
0.0 to 1.0, inclusive, indicating the fractional location from the upper left
corner of the image.
* The user must have the ability to enter text which is to be added to the
image.
* The user must have the ability to enter/select the font size of the text to
be added to the image.
* The user must have the ability to enter/select the color of the text to be 
added to the image.
* The user must have the ability to indicate that they want the entered text
added at the given location in the given font size and color.
* The user must have the ability to remove the most recent text added to the
image.  
* The user must have the ability to clear all texted added to the image.
* The user must have the ability to enter a filename of a different image and
load that image into the GUI for text addition.
* The user must have the ability to click a button to exit the program.
* The GUI must use at least:
  * one label
  * one entry box (entered text must be used somehow by the code)
  * one radio button, checkbox, or dropdown box (the values of these items must
    be used somehow by the game/code)
  * two buttons  (must be linked to some command code)
* More widgets than this minimum are allowed (and will likely be needed) to
implement the needed GUI functions.  Additional GUI features can be added as
needed to ensure the minimum number of widgets and types are used.  

### Approach
1. Sketch out the GUI.  Include all the needed widgets to accomplish the 
  specifications.
2. Follow the instructions under the "Import" heading in the `ImageAnnotationInfo.md` found in
the ImageAnnotation folder for installing and importing the needed `ImageLabel`
widget.
3. Review the `API` section of the README.md file.
4. Start the code for the GUI by defining and placing the needed widgets on
the main window.  Use the `ImageLabel` widget for placing the image on the GUI.
   1. Directly enter the `filename` option during the creation of the 
   `ImageLabel`.  You can use the provided `esophagus2.jpg` file or another of
    your choosing.
   2. Optionally use the `width` option for setting the width of the image to
   fit on your GUI.
5. Connect your widget that allow the user to start the text addition to a
function using the `command` option.  This function should:
   1. Get the entered values for X, Y, text, font size, and color
   2. Call the `ImageLabel.add_text()` function, sending the needed information
   per the API
6. Connect your widget that allows the user to revert the last text addition
to a function using the `command` option.  This function should call the
`ImageLabel.revert_last_addition()` method.
7. Connect your widget that allows the user to clear all text to a function
using the `command` option.  This function should call the 
`ImageLabel.clear_all_text()` function.
8. Modify your code and GUI to allow for the user to
enter a filename to change the image on display.  The 
`tkinter.filedialog.askopenfilename` opens up a dialog box to allow the user
to pick a filename.  The `ImageLabel.load_image()` method can change the
image being displayed.
