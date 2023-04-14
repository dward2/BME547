# `tkinter` Toolbox
## Calling a function after a certain amount of time
You can program `tkinter` to automatically run a function after a
defined period of time.  This is done using the `tkinter.Tk.after()` function.

`tkinter.Tk.after(ms, callback)` will call the function `callback` after `ms`
milliseconds have passed.  Note that program execution does not stop when this
command is reached.  It simply starts a time for the function to be called at
some point in the future.  Also, it only sets this timer once.  After the 
`callback` function is called, it will not be called again in the future unless
another `.after()` is used.

__Example__:
```python
import tkinter as tk
from tkinter import ttk

def make_window():

    def alternate_label():
        if out_label["text"] == "Off":
            out_label.config(text="On")
        else:
            out_label.config(text="Off")
        root.after(3000, alternate_label)

    root = tk.Tk()
    root.title("Example of Using After for Timing")

    out_label = ttk.Label(root, text="Off")
    out_label.grid(column=0, row=0)

    root.after(3000, alternate_label)
    root.mainloop()

if __name__ == '__main__':
    make_window()
``` 
The code above will display a window in which a label is shown with the text
"Off".  Before the `root.mainloop()` is started, an `.after()` command is
used that says to run the function `alternate_label` after 3000 ms (or 3 
seconds).  When those three seconds are passed, `alternate_label` is called
which switches the label from "Off" to "On".  Then, it finishes by issuing
another `.after()` command so that the procedure is run again 3 seconds later.
This will continue until the user closes the window.  

## Intercepting the Close Button
In `tkinter`, clicking on the "close" button in a window's title bar will
call `tkinter` to destroy the window (equivalent to using the `.destroy()`
method on the window widget).  It is possible to change the result of clicking
on the close button by providing your own function that is run when the close
button is clicked.  This is done with the following command:
```python
root.protocol("WM_DELETE_WINDOW", callback)
```
where `root` is the variable of the window widget in question and `callback`
is the name of the function you want to used when the "close" button is
clicked.  Usually, you will want to end the `callback` function with a call to
`root.destroy()` if you want the final action to be to close the window.
