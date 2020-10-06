# Information about updating `git`
## Updating `git`
If you currently have Git for Windows 2.16.1(2) or later installed, you can 
update it to the most recent version from the command line.  Enter 
`git update-git-for-windows` at the command line.

## Changing name of newly defined default branches
In October 2020, GitHub and many other repository hosting sites changed the
default name of the default branch to `main`.  In order to align locally
installed `git` with this change, you can change the default branch name in
`git` as follows:

```
git config --global init.defaultBranch main
```  
