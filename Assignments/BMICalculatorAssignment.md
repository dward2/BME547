# Assignment: BMI Calculator
In this assignment, you will be writing a program to calculate BMI from
inputted weight and height measurements.  GitHub Classroom will be used for
assignment repositories.  Look for the announcement in Sakai with a link.  The
created repository will be empty.  Create a README.md file in GitHub first.
That will allow for this new repository to be cloned to your local computer.

### Program Specifications
* Receives input from the user from the command/terminal window  
   + Input can be received with code such as:   
   `x = input("Enter number: ")`  
   Note that `x` will be a string and may need to be converted to a `float` or
   `int` depending on its use.
   + User must have the option of entering data in either kilograms/meters or
       pounds/inches.  
   
* Outputs to the command/terminal window the calculated BMI  
   + Output can be achieved by code such as:
   `print("The number entered was {}".format(x))`
   
* Outputs whether the calculated BMI represents "underweight",
"normal weight", "overweight", or "obese".  The output must include one of
these four words as written (same capitalization).


### Approach
* Clone GitHub Classroom repository to your computer
* Create feature branch from main branch for new feature to be added 
(e.g., data input)
* Use meaningful commit messages and an appropriate frequency of commits while
developing features.
* Push developed feature branch to GitHub.
* In GitHub, create a Pull request to merge the feature branch into the 
main branch.
* Merge the pull request into main branch.
* Do not delete any of the feature branches.
* In your local repository, checkout the main branch and then pull the newly 
merged main branch back to your local repository so changes to main branch 
in GitHub are captured locally.
* Repeat for other features
* Create a `README.md` file to explain how to run your program from the command
line and how to use your program.  This should be considered a user's manual.
It should explicitly say how to start your program.  For example, "To start
the program, type `python bmi_calc.py` on the command line."
* When the assignment is completed, create an annotated git tag called `v1.0.0`
on your main branch to indicate your final submission.
* If you make additional changes after creating this tag, simply create another
tag (e.g., `v1.0.1`).  We will grade whatever the most recent submission is.
* Make sure your final submission is pushed to GitHub, merged into the
main branch, and tagged before the deadline.


### Grading Criteria
* Good use of `git` workflow  
    + Meaningful commit messages and appropriate number of commits  
    + Use of feature branches, with meaningful names, when adding new 
      functionality
    + Using Pull Requests on GitHub for merging feature branches into main 
      branch
    + All branches and final code pushed to GitHub
    + Use of a git tag
* Python Fundamentals
    + Modular code
    + Code executes without errors
    + Code meets specifications given above
* Presence and content of README.md file

