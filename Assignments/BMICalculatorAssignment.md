# Assignment: BMI/BRI Calculator
In this assignment, you will be writing a program to calculate either BMI (Body 
Mass Index) or BRI (Body Roundness Index) from inputted measurements.  You will 
receive an invitation to a GitHub private repository for use with this assignment. 

### Program Specifications
* Receives the following input from the user in the terminal window:
   + Whether BMI or BRI is to be calculated.
   + Weight and height if BMI is to be calculated.
   + Waist circumference and height if BRI is to be calculated.
   + When entering weight, the user must have the option to enter values in 
     either kilograms or pounds.  
   + When entering height or waist circumference, the user must have the option
     to enter values in either centimeters or inches.
   + Input in either whole or decimal numbers must be allowed.
   + Input can be received with code such as:   
   `x = input("Enter number: ")`  
   Note that `x` will be a string and may need to be converted to a `float` or
   `int` depending on its use.
   
* Outputs to the terminal window the following:
   + If BMI was selected:
     + the calculated BMI
     + classification of the calculated BMI as
  "underweight", "normal weight", "overweight", or "obese".  Use the
  CDC BMI categories as found at https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html.
   + If BRI was selected:
     + the calculated BRI
     + classification of the calculated BRI as:
       + "very lean" if BRI is less than 3.41
       + "lean" if BRI is 3.41 to less than 4.45
       + "average" if BRI is 4.45 to less than 5.46
       + "above average" if BRI is 5.46 to less than 6.91
       + "high" if BRI is 6.91 or greater.
   + For both BMI and BRI, the classification should be outputted exactly as
     spelled and capitalized above.
  
### Approach
* Clone GitHub repository to your computer
* Perform a functional decomposition to design the flow and unit functions 
  needed for your program.
* Document your design using a flowchart or other method.  The design should
  indicate the flow of the program, what functions are needed, and what data
  will be passed to and returned from each function.  This document should be
  committed to your GitHub repository.
* Plan how you are going to break the assignment down into branches.  At 
  least three branches should be used.
* Create a feature branch from main branch for each new feature to be added 
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
* Edit the `README.md` file to contain information about your repository as 
  explained at [Resources/Git/readme_files.md](../Resources/Git/readme_files.md).
  For this assignment, include: 
  * author information
  * a brief description/purpose of the code
  * how to run your program from the command line (For example, "To start
  the program, type `python bmi_calc.py` on the command line.")
  * an explanation for how to use your program (i.e., a user's manual)
  * a link to your design document found in your repository
* Make sure your final submission is pushed to GitHub and fully merged into the
main branch before the deadline.

### `math` Module
For the BRI calculation, you will need to use the `math` module to complete
the calculation.  Watch the Panopto video "Modules" or visit the BME 547
repository [Resources/Python/modules.md](../Resources/Python/modules.md) for 
more information on how to use the `math` module.

### Grading Criteria
* Good use of `git` workflow  
    + Meaningful commit messages and appropriate number of commits  
    + Use of feature branches, with meaningful names, when adding new 
      functionality (must have at least three feature branches)
    + Using Pull Requests on GitHub for merging feature branches into main 
      branch
    + All branches and final code pushed to GitHub
* Modular Design
  * Functional decomposition creates appropriate unit functions
  * Design document clearly documents the flow of the program and shows the
    data passed to and returned from each function
* Python Fundamentals
    + Designed unit functions are correctly implemented
    + Code executes without errors
    + Code meets specifications given above
* Presence and content of README.md file

