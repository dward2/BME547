# Git Concepts
A file in a git repository can be in one of three "places."

When a new file is made in the folder containing the repository,
it is considered in the working copy.  Upon typing `git status`, the following
will show:

```
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        file1.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Once the file is "added" to the repository using `git add <filename>`, it is
now added to the index.  `git status` will now show:
```
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   file1.txt

```

Finally, once the file is committed, it is also then added to the tree, and 
you will then see the following:
```
$ git status
On branch master
nothing to commit, working tree clean

```

If I add a file using `git add <filename>`, and then go to remove it using
`git rm <filename> -f`, the filename is removed from the index and is also
deleted.

On the other hand, `git rm <filename> ,--cached` removes the file from the
index, but does not delete it from the repository folder.  This is the 
opposite of `git add`.

## Removing a file from Repository
Let's say that you accidentally added a file to the repository with a commit.
The safest way to remove it is as follows.
`git rm --cached <filename>` will remove the file from tracking.  Then, if
you commit with `git commit -m "removed <filename>"`, the file will be removed
from the most recent repository, but will still exist in the folder (working
copy).  

An alternate is to reposition the HEAD using `git reset` but could possibly
cause real problems.
For more info, look at <https://stackoverflow.com/questions/5798930/git-rm-cached-x-vs-git-reset-head-x>
 