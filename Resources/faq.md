# Frequently Asked Questions

### Do we need to write unit tests a client function that makes a server request?
If you are making a request to a server of yours that may not be "on" during
testing, **No**, a unit test is not required.  However, it should be handled
the same as a server flask handler function.  It does not need to be tested, 
but make sure the client function only does a minimal amount of work:
   * it gets the data needed to make a server request, 
   * it makes the server request, and
   * gets the response


### Do we need to write unit tests for GUI widget command sub-functions?
**No**, as they cannot be easily be tested outside a working GUI.  The GUI
widget command sub-function should do only three things:  
   * get any needed data from the GUI
   * call an outside function to do the necessary work
   * receive the results of that outside function and update the GUI as needed.  

For example, a sub-function might look like this:

    def ok_button_cmd():
        hdl_value = hdl_entrybox_text.get()  # Gets entered value of an entry box from a StringVar()
        answer = analyze_hdl(hdl_value)      # Class a testable external function to do calculations. 
        result_label[“text”] = answer        # Updates GUI with answer from external function.
        return

### Why do we need both `from tkinter import *` and `from tkinter import ttk`?  Doesn't the first import everything?  And, isn't it bad form to use this syntax? 
*Question*:  
In earlier lectures, you mentioned that imports like `from tkinter 
import *` is not a good practice.  So, why are we importing `tkinter` like 
this? And why do we still need to import `ttk` or `messagebox` after we have
imported all functions in `tkinter`?

*Answer*:  
You are right, it is not a good practice. And, so probably shouldn't 
be done here. But, online, most tutorials and examples for tkinter import it 
this way. So, I just followed suit. Doesn't make it right, but it was just the 
practical response.

As for need to separately import `ttk` and `messagebox`, it has to do with 
functions vs. modules. `tkinter` is a package with a number of functions, for 
example Tk() that defines a root window or StringVar() that makes a string 
variable for use with widgets. `tkinter` also has a number of modules that 
have additional functions inside them. `ttk` is a module of `tkinter` that has 
its own functions such as `Button()` and `Entry()` that create certain widgets.

The statement `from tkinter import *` imports the functions from `tkinter` but 
it does not import the modules. So, if we want to access the functions in one 
of the modules, we need to import the module. Hence, `from tkinter import ttk`. 
But, since we imported the module, and not the functions themselves, we still 
need to append `ttk.` at the start of the function. So, we say 
`ttk.Button()`. Importing `messagebox` is the same. We are importing the module 
`messagebox`, not a function.

You can explore how this is seen in the actual `tkinter` code.  Determine where 
your python installation is on your computer by opening a terminal or command 
window and typing `where python`. It will give you the path where your base 
installation is. Go to that folder. You will see a subfolder there called 
"Lib". Inside of that, you will find a variety of the folders that contain the 
code for all of the base Python packages. One of them will be `tkinter`. If you 
open that, you will see a file called `__init__.py`. This contains the base 
functions of `tkinter` that are imported with the `from tkinter import *` 
statement. You will then also see other modules in this folder like 
`filedailog.py` or `ttk.py`. These modules are imported with statements like
`from tkinter import ttk`.

For a more detailed explanation of all of this, see the Python documentation 
on packages at <https://docs.python.org/3/tutorial/modules.html#packages>.
