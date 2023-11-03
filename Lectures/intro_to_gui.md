# Graphical User Interface (GUI)

## Intro
Typically, we think of computer programs as being sequential:  moving
from one block to another, each block transforming inputs to outputs, with
continuous "action".

GUIs are typically "reactive" or event driven.  After the initial display of
the GUI, the program generally waits for some sort
of user input.  That input triggers some code to take an action leading to 
modified output in the GUI.  Then, the program waits for more user input.

Another example of event-driven interactions is the server-client relationship.
Once a server is started, it essentially waits for a request from a client.
The client request triggers specific server code to act on that request.

__What are GUI events?__  Clicking on a button, entering text in a field,
dragging a scroll bar, making a choice from a menu, moving the mouse, etc.

In sum, the user causes an event to happen, and the program responds to these 
events.

## Principles for GUI Interface Design
* __Make things cancelable or reversible__  
Give the user the option to cancel an action at
any step of the process.  There is nothing more frustrating than clicking on
something, realizing you don't want to do it, and having no option but to
move forward with something you didn't want to do.  Also, a more forgiving
interface will encourage a user to do more exploration.

* __Provide frequent feedback__  
Tell users when an action is complete and what
was done or completed during that action.

* __Create cues about what should be done next__  
   + Use checklists or label steps
   + Put the  next action or input near to the previous action or input
  
* __Be consistent in how interface works__
  
* __Avoid jargon__  
  Make sure that actions or input required are understood.

## GUIs for Python
There are a very large number of GUI packages for use in Python. 
[See a list here.](https://wiki.python.org/moin/GuiProgramming)

Most are a set of Python bindings to an underlying graphics package that often
provides support for multiple platforms.  Two such packages are:
* [Tkinter](https://docs.python.org/3/library/tk.html): a package bundled with 
default Python distribution that binds to the open-source, cross-platform 
GUI toolkit [Tk](https://en.wikipedia.org/wiki/Tk_(software)).
* [PyQt](https://www.riverbankcomputing.com/software/pyqt/intro): 
a Python binding to the [Qt](https://www.qt.io/) framework, a popular 
cross-platform GUI framework written in C++.

A lot goes into deciding the best GUI package to use:  the needed 
functionality, licensing considerations, easy of use, and personal preferences.

In class, we will be discussing the use of the `tkinter` package as it is
relatively easy to use and is part of the Python install.

