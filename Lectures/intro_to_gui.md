# Graphical User Interface (GUI)

## Notes
Typically, we think of computer programs as being sequential:  moving
from one block to another, each block transforming inputs to outputs.

GUIs are more "reactive" or event driven.  Program waits for some sort
of user input.  That input causes and action leading to an output.

Other event driven things:  server-client, user - program, OS - kernel

What are GUI events?  Clicking on a button, entering text in a field,
dragging a scroll bar, making choice from menu

User causes event to happen, and the program responds to these events.

<http://zetcode.com/gui/pyqt5/introduction/>

<https://pythonspot.com/pyqt5/>

<https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html>

<https://tkdocs.com/tutorial/>

Discuss how you might want to map out your interface, understand how it can
be gridded, before getting started.

## Ideals for GUI Interface
* Make things cancelable.  Give the user the option to cancel an action at
any step of the process.  There is nothing more frustrating than clicking on
something, realizing you don't want to do it, and having no option but to
move forward with something you didn't want to do.

* Provide frequent feedback.  Tell users when an action is complete and what
was done during that action.

* Place users in control of interface  
  + Make actions reversible:  allows user to explore interface
  + Create cues about what should be done next:  use checklists, put the
  next action or input near to the previous action or input
  + Be consistent in how interface works
  
* Avoid jargon.  Make sure that actions or input required are understood.

## Tk Info
When making a widget, you must always specify the parent when defining the
Widget.  The parent is the widget in which you want to place the new widget.
For example:
```
root = Tk() # Defines the top, or root, window, so doesn't have a parent
content = ttk.Frame(root)  # The content Frame is placed in root
button = ttk.Button(content) # The button button is placed in the content
```
  
Widgets are configured when first created by sending parameters after the
parent.  Example:
```
>>> button.ttk.Button(root, text="Hello", command="buttonpressed")
```
You can then see the values of the configurations as so:
```
>>> button['text']
'Hello'
```
We can change the value of certain configurations as follows:
```
>>> button['text'] = 'goodbye'
# Or another way is
>>> button.configure(text='goodbye')
>>> button['text']
'goodbye'
```
We can get more information about a particular configuration as follows:
```
>>> button.configure('text')
('text', 'text', 'Text', '', 'goodbye')
```
Or, a list of all of the configuration options:
```
>>> button.configure()
{'command': ('command', 'command', 'Command', '', 'buttonpressed'),
 'default': ('default', 'default', 'Default', <index object: 'normal'>, <index object: 'normal'>),
 'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', 'ttk::takefocus', 'ttk::takefocus'),
 'text': ('text', 'text', 'Text', '', 'goodbye'),
 'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''),
 'underline': ('underline', 'underline', 'Underline', -1, -1),
 'width': ('width', 'width', 'Width', '', ''),
 'image': ('image', 'image', 'Image', '', ''),
 'compound': ('compound', 'compound', 'Compound', <index object: 'none'>, <index object: 'none'>),
 'padding': ('padding', 'padding', 'Pad', '', ''),
 'state': ('state', 'state', 'State', <index object: 'normal'>, <index object: 'normal'>),
 'cursor': ('cursor', 'cursor', 'Cursor', '', ''),
 'style': ('style', 'style', 'Style', '', ''),
 'class': ('class', '', '', '', '')}
```

Need to create a Widget, and then put it in window in the right place.  This
is called Geometry Management.  The `grid` command above is a type of 
geometry manager.  

### Widgets of Interest
* Frame  
    + `frame = ttk.Frame(parent)`
    + Normally, it will size based on widgets put in it.  But, if you want
    empty frame, or define its size, use `width` and `height`.  When specifying
    sizes, `350` means 350 pixels, `350c` means 350 centimeters, `350i` means
    350 inches, and `350p` means 350 printer's points (1/72 inch).
    + `frame['padding'] = (5, 10)` requests extra space around inside of frame.
    A single number is for all sides, two numbers are horiz/vertical, four
    numbers specify left, top, right, bottom.
    + frame['borderwidth'] = 0` where 0 (default) is no border, or positive
    number is width of border.
    + `frame['relief'] = 'sunken'` sets frame style with options `flat`
    (default), `raised`, `sunken`, `solid`, `ridge`, or `groove`.
* Label
    + `label = ttk.Label(parent, text='text for label')`
    + To attach a variable text string to a label:
    ````
    resultsContents = StringVar()
    label['textvariable'] = resultsContents
    resultsContents.set('New value to display')
    ````
* Button
    + `button = ttk.Button(parent, text='Okay', command=submitForm)`
    + `button.state(['disabled'])`  # disables button
    + 'button.state(['!disabled'])'  # enables button
    + `button.instate[['disabled' | '!disabled']]`  # returns true if the
    specified flag is the current state.
    + `button.instate(['!disabled'], cmd)`  # runs cmd if button state enabled
* Checkbutton
    + ```
      measureSystem = StringVar()
      check = ttk.Checkbutton(parent, text='Use Metric',
                  command=metricChanged, variable=measureSystem,
                  onvalue='metric', offvalue='imperial')
      ```
    + `check['variable']` returns value of checkbox.  Default of 1 if checked,
    0 if not.  But, these values of 1 and 0 are changed by `onvalue` and 
    `offvalue`
* Radiobutton
    + ```
      phone = StringVar()
      home = ttk.Radiobutton(parent, text='Home', variable=phone, value='home')
      office = ttk.Radiobutton(parent, text='Office', variable=phone, value='office'
      cell = ttk.Radiobutton(parent, text='Mobile', variable=phone, value='cell')
      ```
* Entry
    + ```
      username = StringVar()
      name = ttk.Entry(parent, textvariable=username)
      ```
    + `width` option specifies number of characters wide for field.
    + `name.get()` returns current value in field
    + `name.delete(0, 'end')` deletes between the two indices
    + `name.insert(0, 'your name')` inserts new text at given index
    + `show='*'` configuration can be used for password entry
* Combobox
    + ```
      countryvar = StringVar()
      country = ttk.Combobox(parent, textvariable=countryvar)
      ```
    + `get` and `set` methods are used to set value
    + `country.bind('<<ComboboxSelected>>', function)` will call function 
    whenever value of combobox changes.
    + `country['values'] = ('USA', 'Canada', 'Mexico')` will populate list of 
    values users can choose from.  `readonly` state flag will force choice
    from this list.
    + `current()` method determines which item in predefined values list is 
    selected.