# Notepad++
Website:  https://notepad-plus-plus.org/

Notepad++ is a free code / text editor for Windows.  It has functionality
for highlighting syntax for a variety of different programming languages.
Plug-ins exist to allow for easy comparison of changes between files and 
rendering Markdown language.

For Windows, I would recommend using the 32-bit version as it provides the best
compatibility with plug-ins.

## Tips for Using Notepad++
### Converting tabs to spaces
As the PEP-8 style convention prefers using spaces for indentation rather than
tabs, it is best to change the setting in Notepad++ such that hitting tab 
actually inserts spaces.  

This setting can be found by going to the "Settings" menu and selecting
"Preferences...". The "Preferences" window will open. Choose "Indentation"
from the list on the left side of the window. Then, you will see an "Indent 
Settings" box in the center of the window.  Under "Indent using:", select the
"Space character(s)" radio button.  (Note, these
steps taken from v8.8.8.  In some earlier versions, this option was found on
the "Language" section of the Preferences window).

Note that Notepad++ will autoindent to match the indentation of previous lines.
Unfortunately, this may cause some PEP-8 style conflicts for blank lines.  Scan
for these when checking code style.

### Markdown viewer
Plug-ins are available that allow Markdown files to be rendered in Notepad++.
One such viewer is recommended in the [markdown.md](markdown.md) file.
