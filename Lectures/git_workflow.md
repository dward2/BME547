# Git Workflow
## Feature Branch Approach
In this approach, each major feature of the software is developed on its own
branch in git.  Once the feature is complete, tested, and approved, it can
then be merged into the master branch.  No development should be done directly
on the master branch.  In this way, the master branch always contains the 
latest, correctly working copy of the program.

Code development on each feature should be kept reasonably independent from 
other features and branches.

## When to Commit
A commit should represent a discrete piece of work or code, not a hodgepodge
of changes.  When writing new code, at a minimum each new function should be
its own commit.  When fixing bugs, each bug fix should be one commit.  Or, if
it is a major bug requiring lots of changes, the bug fix might be done on a
branch with multiple commits for when each function is changed.

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
<td>Fixed bug where typing 'a' in interface led to crash in function 'addition"</td>
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
<table>

## Example of branch/commit design
Lets say you were working on a calculator app.  You might choose to develop
the user interface on the `interface` branch, and the code to do the math on 
a different branch called `calculation`.  On the `calculation` branch, you 
might have one commit be the function for doing addition, and another commit
for the function doing subtraction, etc.

Alternatively, you might choose to do the branches differently, such as
developing the addition on a single branch, and the commits could be the code
for doing the math and then the code for the interface.  Subtraction would be
developed on a different branch.

## Exercise

* Create a GitHub repository with a `README.md` file
* Clone repository to your local computer
* Create a virtual environment
* Create branch called `interface`
* Create a file and add the following code for the interface
```python
def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    if choice=='9':
        return
   
if __name__ == '__main__':
        interface()
```
* Commit and run to test.
* Modify so that it continues until quit is hit.
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
* Commit
* Push Branch to GitHub
* On GitHub, do Pull Request
* Locally, pull new master to local.
* From master, create a new branch called `addition`.
* Write function for addition:
```python
def addition(a, b):
    answer = a + b
    return answer
```
* Commit
Write function to accept inputs:
```python
def addition_interface():
    print("Addition")
    input1 = input("Enter the first number: ")
    input2 = input("Enter the second number: ")
    number1 = int(input1)
    number2 = int(input2)
    result = addition(number1, number2)
    print("The answer is {}".format(result))
    return

```
* Commit
* Modify interface to add the addition option:
```python
def interface():
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options:")
        print("1 - Addition")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keep_running = False
        elif choice == '1':
            addition_interface()
    return
```
* Commit
* Test and make sure additional feature works.
* Push `addition` branch to GitHub.
* On GitHub, open a Pull Request to merge `addition` into `master`.

### Continue Exercise
* Find a partner and give permission for them to access your repository
* Clone your partner's repository and using the feature branch approach, add
a subtraction feature to their code.
* Push the new branch to their GitHub repository.
* Open a Pull Request and include your partner as a reviewer.  Do not merge
the Pull Request.  That is up to the partner who owns the repository.



