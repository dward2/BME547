# Creating a GUI in `tkinter`
This page will go through all of the steps for how to code a GUI in Python
using `tkinter`.  This is simply one approach of many and can be used for
one-window interfaces and allows for easy testing of any logic code that
supports the interface.

## General Code Layout
This code describes a suggested layout for your GUI code.
```python
# Import Statements
import tkinter as tk
from tkinter import ttk

"""
************* LOGIC FUNCTIONS ************************************************
Define here any functions that are needed to do the "logic" or algorithmic
work for your GUI.  These functions should include the things that will
need unit testing.

If preferred, these functions can be in a separate module and then
imported into this module.

The input parameters to these functions should contain whatever information was
entered into the GUI and needed for the work

The functions should return whatever information is needed by the GUI to
update.
"""
def example_logic_function(input):
    result = do_work_on_input(input)
    return result

"""
************* END LOGIC FUNCTIONS ********************************************

************* MAIN WINDOW CREATION *******************************************
Define here a "main_window" function that will create the root window, add all 
of the necessary widgets to the window, and contain the command functions that 
provide functionality to the widgets.
"""
def main_window():
    
    """
    ***************** Command Functions ********************************
    Define here any sub-functions in the "main_window" function that are
    needed as "command" functions for the various widgets.  For example,
    one command function will likely be linked to a button that when the
    user clicks on it causes the GUI to take some sort of action.

    These command functions should generally only do three things:
    1) Get the needed information from the GUI
    2) Call outside functions that do the actual work, sending the needed
       GUI data to those functions as parameters, and receiving results from
       those functions
    3) Update the GUI based on the results

    These sub-functions cannot be tested and so should not contain any
    algorithmic work that is not directly GUI related.

    """
    def example_command_function():
        name = user_name_variable.get()
        answer = example_logic_function(name)
        output_label.configure(text="Got an answer")

    """
    ***************** END Command Functions ****************************
    
    ***************** Define GUI & Widgets *****************************
    Here in the main body of the "main_window" function, create the 
    root window and add the necessary widgets to the window
    """
    
    # Define root window
    root = tk.Tk()
    root.title("My GUI")
    
    # Add widgets
    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=0)
    
    user_name_variable = tk.StringVar()
    user_name_entry = ttk.Entry(root, textvariable=user_name_variable)
    user_name_entry.grid(column=1, row=0)
    
    output_label = ttk.Label(root, text="Output")
    output_label.grid(column=0, row=1, columnspan=2)
    
    ok_button = ttk.Button(root, text="Ok", command=example_command_function)
    ok_button.grid(column=2, row=1)
    
    """
    ***************** END Define GUI & WIDGETS *************************
    
    ***************** Start GUI *****************************
    The last thing that should be done in the "main_window" function is to 
    start the GUI using the ".mainloop" method of the root window.  Any code
    that is entered after this command will only happen after the GUI is closed
    when the root window is closed.
    """
    root.mainloop()
    print("Program is done")
    

"""
************* END MAIN WINDOW CREATION****************************************

************* START PROGRAM **************************************************
The program is started here.  You could add calls to other set-up functions,
like connecting to a database here:
"""
if __name__ == "__main__":
    call_other_setup_functions()
    main_window()
```