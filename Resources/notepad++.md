# Notepad++
Website:  https://notepad-plus-plus.org/

Notepad++ is a free code / text editor for Windows.  It has functionality
for highlighting syntax for a variety of different programming languages.
Plug-ins exist to allow for easy comparison of changes between files and 
rendering Markdown language.

## Tips for Using Notepad++
### Converting tabs to spaces
As the PEP-8 style convention prefers using spaces for indentation rather than
tabs, it is best to change the setting in Notepad++ such that hitting tab 
actually inserts spaces.  

This setting can be found by selecting "Preferences..." under the "Settings"
menu.  The "Preferences" window will open.  Choose "Language" from the list
on the left side of the window.  Then, you will see a box labelled "Tab 
Settings".  Click on the "Replace by space" check box. (Note, these steps
taken from v7.5.9, but are hopefully valid for all versions).

Note that Notepad++ will autoindent to match the indentation of previous lines.
Unfortunately, this may cause some PEP-8 style conflicts for blank lines.  Scan
for these when checking code style.

### Markdown viewer
Plug-ins are available that allow Markdown files to be rendered in Notepad++.
One such viewer is recommended in the [markdown.md](markdown.md) file.
