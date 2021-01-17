# Adding `git` branch to macOS terminal prompt

In order to see the current `git` branch in the macOS terminal prompt,
do the following:

## For mac OS 10.15 (Catalina) or later

With the update to MacOS Catalina, Apple changed the default shell to zsh, so the code will goto .zshrc instead of .bashrc.

* Look to see if the file `~/.zshrc` exists.
* If it does not, create it with `touch ~/.zshrc`.
* Open `~/.zshrc` in your favorite text editor.
* Add the following content:  

```
# Load vcs information
autoload -Uz vcs_info
precmd() { vcs_info }
# Format the vcs_info_msg_0_ variable
COLOR_DEF=$'\e[0m'
COLOR_GIT=$'\e[38;5;39m'
zstyle ':vcs_info:git:*' formats ${COLOR_GIT}'(%b)'${COLOR_DEF}
 
# Setup the prompt with git branch name
setopt PROMPT_SUBST
PROMPT='%n@%m in ${PWD/#$HOME/~} ${vcs_info_msg_0_} > '
```
Now run `source ~/.zshrc` in your Terminal to see the changes.
* Note:
If ~/.zshrc not there then run mv ~/.bashrc ~/.zshrc and mv ~/.bash_profile ~/.zprofile

### Reference
This information was taken from 
<https://medium.com/@sreedhu7/show-git-branch-name-in-terminal-macos-catalina-625a69ecb2c9>

## For mac OS 10.14 (Mojave) or earlier

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

### Reference
This information was taken from 
<https://www.mfitzp.com/article/add-git-branch-name-to-terminal-prompt-mac/>
