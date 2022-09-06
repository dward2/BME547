# Git Feature Branch Workflow Overview

* In your local repository, start on the `main` branch.
* Create a new feature branch  
  `git branch <new_feature>`
* Checkout the new feature branch  
  `git checkout <new_feature>`
* Develop code
  + Write/test some code
  + Add / Commit code to repository  
    `git add <files>`  
    `git commit -m <commit_message>`  
  + Repeat until feature is completed
* Push code to GitHub  
  `git push set-upstream origin <new_feature>`
* On GitHub, create a Pull Request to merge the new feature branch into the
  main branch.  Then, complete the merge.
* In your local repository, checkout the main branch.  
  `git checkout main`
* Pull the merged changes from GitHub into your local repository.  
  `git pull`