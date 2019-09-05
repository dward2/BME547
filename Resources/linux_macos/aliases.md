# Aliases

In linux or macOS, you can create an alias for use at the command line.  For
example, if the `python` command opens Python version 2 and the `python3`
command opens Python version 3, we can add an alias such that typing
`python` will actually open Python version 3.  (Note: procedures for making
aliases in Windows and GitBash are different than these.)

## MacOS

* In the terminal, type `cd ~` to ensure you are in your home directory.
* Type `ls -a` to list all files in this directory, including those that are
hidden.  One of the files should be `.bash_profile`.
* Open `.bash_profile` for editing in your favorite text editor.
* Add the following line: `alias python='python3'`
* Save and close the file.
* Close and then re-open your terminal window to have the new alias take
effect.
  
Now, the command `python` should run Python version 3.  

Note, you can make an alias for any command line command.

## Linux
+ In the terminal, type `cd ~` to ensure you are in your home directory.
+ Type `ls -a` to list all files in this directory, including those that are
hidden.  One of the files should be `.bashrc`.
+ Open `.bashrc` for editing in your favorite text editor.
+ Look to see if the following lines are in the file:    
  ```
  if [ -f ~/.bash_aliases ]; then
      . ~/.bash_aliases
  fi
  ```  
  If so, do the following:
  
    - Close `.bashrc` and see if the file `.bash_aliases` exists in your
      home directory.  If not, create a file called `.bash_aliases`.
    - Open `.bash_aliases` in your favorite text editor.
  
+ In either `.bashrc` or `.bash_aliases`, add the following line: `alias python=python3`
+ Save and close the file.
+ To make the aliases active, you can do one of two things:
  - Close and then re-open your terminal window, or
  - Enter the command `source .bashrc` at the command line.
  
Now, the command `python` should run Python version 3.  

Note, you can make an alias for any command line command.

## Bypassing Alias
If you temporarily do not want to use the alias, but in fact want to command
you entered to be used without the alias, you can enter the command with the
\ symbol before it.

For example, above, an alias was defined as `alias python='python3'` for macOS
such that:
```
Work@Evans-MacBook-Pro ~ $ python -V
Python 3.6.5
```

But, if it desired to run the original `python` command without the alias,
enter:
```
Work@Evans-MacBook-Pro ~ $ \python -V
Python 2.7.10
```