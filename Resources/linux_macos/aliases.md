# Aliases

In linux or macOS, you can create an alias for use at the command line.  For
example, if the `python` command opens Python version 2 and the `python3`
command opens Python version 3, we can add an alias such that typing
`python` will actually open Python version 3.

* In the terminal, type `cd ~` to ensure you are in your home directory.
* Type `ls -a` to list all files in this directory, including those that are
hidden.  One of the files should be `.bash_profile`.
* Open `.bash_profile` for editing in your favorite text editor.
* Add the following line: `python=python3`
* Save and close the file.
* Close and then re-open your terminal window to have the new alias take
effect.
  
Now, the command `python` should run Python version 3.  

Note, you can make an alias for any command line command.