# Checking Out Branches When There are Uncommitted Changes

Scenario:  You create a feature branch from the `main` branch.  On this
feature branch, you make some changes, but do not commit those changes to the
repository.  You then try to go back and checkout the `main` branch.  One of 
two results will occur:
1. git will allow the checkout and will "carry" any uncommitted changes from
the feature branch to the `main` branch.
2. git will not allow the checkout and you will get an error message that may
look something like this:
   ```
   error: Your local changes to the following files would be overwritten by checkout:
        HDL.md
   Please commit your changes or stash them before you switch branches.
   Aborting
   ```
   
*When does git allow the checkout and when does it not?*

### When is it allowed?
For each file that has uncommitted changes on the feature branch, if the most
recent commit of the file on the feature branch has identical contents to the
most recent commit on the `main` branch, git will allow the checkout.

When the committed contents of two branches are the same, if you checkout the
other branch with some uncommitted changes, git assumes that you mistakenly
started working on one branch when you really wanted to be working on another
branch.  So, it takes these uncommitted changes with you from one branch to
another.  (Note, this is my interpretation of the intention and may not fully
explain the reasoning for this behavior in git.)  The changes remain 
uncommitted on the checked out branch.

### When is it not allowed?
For each file that has uncommitted changes on the feature branch, if the most
recent commit of the file on the feature branch has different content than the
most recent commit on the `main` branch, git will not allow the checkout.

When the committed contents of two branches are not the same, when you try
and checkout the other branch, it is not clear to git whether the uncommitted
changes you have made on the contents of the current branch are applicable to
the different contents on the other branch.  So, git refuses the checkout.

### Examples
#### Checkout Allowed
A repository starts with three files committed.
```
dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (main)
$ ls
HDL.md  LDL.md  README.md

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (main)
$ git status
On branch main
nothing to commit, working tree clean
```
The file `HDL.md` contains the single word "Contents".

Next a feature branch called "test_info" is made and checked out.
```
dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (main)
$ git branch test_info

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (main)
$ git checkout test_info
Switched to branch 'test_info'

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ ls
HDL.md  LDL.md  README.md

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git status
On branch test_info
nothing to commit, working tree clean
```
The `HDL.md` file is edited so that it now contains the single word "Supplies".
This will cause an uncommitted change to be observed by git.

```
dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git status
On branch test_info
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   HDL.md

no changes added to commit (use "git add" and/or "git commit -a")
```

With this uncommitted change, the command is given to checkout the `main`
branch:

```
dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git checkout main
Switched to branch 'main'
M       HDL.md
```
Since the contents of the `HDL.md` file on the `main` branch are the same as
the contents of the committed `HDL.md` file on the `test_info` branch, the 
checkout is allowed.  The uncommitted changes made on the feature branch
are now found on the `main` branch.  Note that the output indicates that the
`HDL.md` file has been (M)odified relative to the committed contents of the
repository.  It is still uncommitted, so the repository contents of the `main`
branch itself still doesn't have the change.

```
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   HDL.md

no changes added to commit (use "git add" and/or "git commit -a")
```

The changes can either now be committed to the `main` branch or reverted by 
using the `git restore` command.

#### Checkout Not Allowed
Again, assume a repository with three committed files, and the `HDL.md` file
contains the single word "Contents".

```
dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (main)
$ ls
HDL.md  LDL.md  README.md

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (main)
$ git status
On branch main
nothing to commit, working tree clean
```

Next a feature branch called "test_info" is made and checked out.
```
dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (main)
$ git branch test_info

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (main)
$ git checkout test_info
Switched to branch 'test_info'

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ ls
HDL.md  LDL.md  README.md

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git status
On branch test_info
nothing to commit, working tree clean
```
The `HDL.md` file is edited so that it now contains the single word "Supplies".
The contents of the `HDL.md` are modified and then this modified file is 
committed to the `test_info` branch of the repository.

```
dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ nano HDL.md

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git status
On branch test_info
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   HDL.md

no changes added to commit (use "git add" and/or "git commit -a")

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git add HDL.md

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git commit -m "Modified contents of HDL.md"
[test_info 35945a4] Modified contents of HDL.md
 1 file changed, 1 insertion(+), 1 deletion(-)

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git status
On branch test_info
nothing to commit, working tree clean
```

Now, another change is made to the `HDL.md` file, but this change is not
committed to the branch.

```
dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ nano HDL.md

dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git status
On branch test_info
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   HDL.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Then, an attempt is made to checkout the `main` branch.
```
dwonl@DESKTOP-G8L84L6 MINGW64 /d/ClassRepos/git_branches (test_info)
$ git checkout main
error: Your local changes to the following files would be overwritten by checkout:
        HDL.md
Please commit your changes or stash them before you switch branches.
Aborting
```
The checkout is not allowed by git because the committed contents of `HDL.md` 
on the `main` branch do not match the last committed conetns from the 
`test_info` branch.  To do the checkout, you must either revert the changes by
using `git restore` or commit the changes to the branch in order to be able to
checkout the `main` branch.

### Deleted Files
The same situations can happen when dealing with a deleted file.  If you delete
a file from a branch, but do not commit the deletion, switching to another
branch may bring the uncommitted deletion to the checked out branch.  So, it
would appear that the file has been deleted on the checked out branch, but this
is an uncommitted deletion and can be reverted by using `git restore` if
desired.
