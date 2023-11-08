## Image Annotation
Write GUI code that allows a user to add text annotations to a medical image.
A custom widget called `ImageLabel` is provided that has functionality to
display an image and add text to it.

### Approach
1. Sketch out the GUI.  On the interface you will want 
   1. a place to display the image 
   2. the ability for the user to input X and Y coordinates, which will be
   floats from 0.0 to 1.0, indicating the fractional location from the upper
   left corner of the image
   3. the ability for the user to enter text to add to the image
   4. the ability for the user to enter/select the font size
   5. the ability for the user to enter/select the text color
   6. the ability for the user to indicate that they want to add the entered
   text to the image at the entered location, font size, and color
   6. the ability for the user to indicate they want to remove the most
   recent text added to the image
   7. the ability for the user to clear all text from the image
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
8. If you like, you could modify your code and GUI to allow for the user to
enter a filename to change the image on display.  The 
`tkinter.filedialog.askopenfilename` opens up a dialog box to allow the user
to pick a filename.  The `ImageLabel.load_image()` method can change the
image being displayed.
