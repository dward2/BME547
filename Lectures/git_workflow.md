# Git Workflow
## Feature Branch Approach
![](./lecture_files/branching.png)
In this approach, each major feature of the software is developed on its own
branch in git.  Once the feature is complete, tested, and approved, it can
then be merged into the main branch.  No development should be done directly
on the main branch.  In this way, the main branch always contains the 
latest, correctly working copy of the program.

Code development on each feature should be kept reasonably independent of 
other features and branches.

## When to Commit
A commit should represent a discrete piece of work or code, not a hodgepodge of
changes. When writing new code, a rule of thumb would be making a commit for
each new function written. When fixing bugs, each bug fix should be one commit.
Or, if it is a major bug requiring lots of changes, the bug fix might be done
on a branch with multiple commits where each commit is a step towards fixing
the bug.

Commit messages should describe what is added or changed in the program and,
most importantly, why.  A message like "fixed bug" does not
communicate anything.  Whereas "fixed bug where typing 'a' in interface led
to crash in function 'addition'" is better.  

<table>
<tr>
<th>Bad Commit Message</th>
<th>Good Commit Message</th>
</tr>

<tr>
<td>Fixed bug</td>
<td>Fixed bug where typing 'a' in interface led to crash in function 'addition'</td>
</tr>

<tr>
<td>Added new code</td>
<td>Implement multiplication function in calculator</td>
</tr>

<tr>
<td> Working more on feature</td>
<td> Add two buttons to GUI to allow for scrolling through list</td>
</tr>

<tr>
<td>Change pt_limit from 5 to 10</td>
<td>Extended the number of points that will be plotted by changing constant pt_limit</td>
</tr>
</table>

## Example of branch/commit design
Let's say you were working on a calculator app.  You might choose to develop
the user interface on the `interface` branch, and the code to do the math on 
a different branch called `calculation`.  On the `calculation` branch, you 
might have one commit be the function for doing addition, and another commit
for the function doing subtraction, etc.

Alternatively, you might choose to do the branches differently, such as
developing the addition on a single branch, and the commits could be the code
for doing the math and then the code for the interface.  Subtraction would be
developed on a different branch.

## Class Activity
Let's write a program that will analyze some basic laboratory blood test 
results.

### Specifications
* Allows user to select the type of test (HDL vs LDL vs Total)
* Allows user to enter the test result
* Calculates whether the entered test results is in or out of desired ranges
* Outputs the result to the user

### Interface Branch
* In your classwork repository, create and checkout a branch called `interface`
* Create a file and add the following code for the interface
```python
def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    if choice=='9':
        return
   
interface()
```
* Run code to test, then commit it to repository.
* Modify code, using a `while` loop, so that it continues until quit is hit.
<!---
```python
def interface():
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keep_running = False
    return
   
```
--->
* Commit
* Push Branch to GitHub
* On GitHub, open Pull Request to merge `interface` into `main`.
* Confirm Pull Request.
* On local computer, checkout `main` and pull the updated `main` branch 
from GitHub to your local repository.

### HDL Branch
The first check will be categorizing the results of an HDL test.
* From `main`, create and checkout a new branch called `HDL`.
* To the `while` loop of the interface, add code to allow user to select an
  HDL test and have it call a yet-to-be-written function called `hdl_driver`.

**EXERCISE NO. 1**
* Write the following three functions:
  * `input_HDL_value` to accept user input and return a value the 
    inputted value
  * `check_HDL` which receives the HDL value as input and returns a string
    based on the following table:
    <table>
    <tr>
    <th>If HDL Is</th> <th>Return</th>
    </tr>
    <tr>
    <td> 60 or greater</td> <td>"Normal"</td>
    </tr>
    <tr>
    <td>40 or greater but less than 60</td> <td>"Borderline Low"</td>
    </tr>
    <tr>
    <td>below 40</td> <td>"Low"</td>
    </tr>
    
    </table>
    
  * `output_HDL_result` which receives the string from above and prints it 
    on the
    screen.
  * `hdl_driver` that calls the three functions above, receiving and sending 
    the needed values. 
* Make sure to make a commit to the repository after writing each function.
* Test everything, and make changes as needed.  Commit any changes.
* Push `HDL` branch to GitHub.
* On GitHub, open a Pull Request to merge `HDL` into `main`.
* Confirm pull request.
* Pull updated `main` branch to local repository.

### LDL Branch

**EXERCISE NO. 2**

Make an `LDL` branch and do the same thing as in the HDL branch and Exercise No.
1, but now for LDL.  The LDL classification is as shown below:

| If LDL is                       | Return            |
|---------------------------------|-------------------|
| Less than 130                   | "Normal"          |
| 130 or higher but less than 160 | "Borderline High" |
| 160 or higher but less than 190 | "High"            |
| 190 or greater                  | "Very High"       |


### Total Cholesterol Branch

**Additional Practice**
* Using the feature branch approach, add a total cholesterol check feature 
to your code.

| If Total Cholesterol is         | Return            |
|---------------------------------|-------------------|
| Less than 200                   | "Normal"          |
| 200 or higher but less than 240 | "Borderline High" |
| 240 or greater                  | "High"            |

  