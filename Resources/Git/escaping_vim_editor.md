# Escaping the VIM editor when making a git commit

<http://www.commitstrip.com/en/2017/05/29/trapped/>

When making a `git commit`, if you do not specify a commit message on the
command line by using `git commit -m "replace with your commit message"`, your
default text editor will be opened for you to type in a commit message.
Depending on your set-up, `vim` may be your default text editor.  Below
are the commands necessary to enter your commit message and exit `vim`.

* Go to the first line of the file and enter your commit message.
* If you cannot enter anything, look to see if `-- INSERT --` is showing.  If
it is not, you enter INSERT mode by typing `i`.
* Exit INSERT mode by pressing `ESC`.
* Type `:wq` and press enter.  That should save the commit message and exit 
`vim`.


Note:  `:` enters command mode, `w` writes the files, and `q` quits the editor.

For more information, visit the site this information was taken from:

<https://apple.stackexchange.com/questions/252541/how-do-i-escape-the-git-commit-window-from-os-x-terminal>

