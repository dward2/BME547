# Adding `git` branch to macOS terminal prompt

In order to see the current `git` branch in the macOS terminal prompt,
do the following:

* Look to see if the file `~/.bash_profile` exists.
* If it does not, create it with `touch ~/.bash_profile`.
* Open `~/.bash_profile` in your favorite text editor.
* Add the following content:
```
# Git branch in prompt.

parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

export PS1="\u@\h \W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "
```
* Close the terminal window and re-open it.  If you now navigate to a `git`
repository, you should see the branch name.
* Note, if for some reason you do not want to close your terminal window
after making the change to `~/.bash_profile`, you can type 
`source ~/.bash_profile` to activate the changes.

## Reference
This information was taken from 
<https://www.mfitzp.com/article/add-git-branch-name-to-terminal-prompt-mac/>