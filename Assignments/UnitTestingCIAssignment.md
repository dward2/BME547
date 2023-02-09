# Unit Testing and Continuous Integration

In this assignment, you will write a function and comprehensive unit tests to
ensure the function meets specifications.  You will also configure Continuous
Integration (CI) to automatically run tests on push and pull request events.

See Sakai for GitHub Classroom link and due date.

### Background
Assume you are part of the development team for a medical system input device
that is meant to take handwritten information from an input screen, convert
the handwriting to text using character recognition algorithms, and store the 
information in the appropriate database.  You have been tasked to write a 
function that analyzes the text obtained from the e-mail entry field.  You will 
need to examine the string that should contain an e-mail and interpret whether 
it is a valid e-mail.  The quality of the character recognition may not be 
perfect.  Therefore, any code that is looking to interpret the results needs to 
be flexible enough to read results that may be slightly off.   

### Function Specifications
* The function should be named `is_email` and located in a module called 
`email_checker.py`.
* The function should receive a single parameter containing the string to 
  check.
* The function should return a boolean value.
  + The boolean value should be `True` if the string sent to the function 
    contains a valid e-mail address.  
  + The boolean value should be `False` if it does not.
* An acceptable e-mail is:
  * in the format of **prefix@domain.toplevel**
  * the **prefix**
    * contains only letters (a-z, A-Z), numbers (0-9), underscores (_), 
      periods (.), and dashes (-)  
    * does not start or end with an underscore, period, or dash
    * does not contain any consecutive underscores, periods, and dashes 
      (i.e., "david..ward" is unacceptable, but "david.-ward" is)
  * the **domain**
    * contains only letters (a-z, A-Z), numbers (0-9), and dashes (-)
    * does not start or end with a dash
    * does not contain any consecutive dashes
  * the **toplevel**
    * contains only letters (a-z, A-Z)
    * consists of at least two letters
* The input string may have spaces incorrectly added by the character
  recognition that should not be considered part of the email.  These include:
  * One or more spaces at the start of the string before the **prefix**
  * One or more spaces at the end of the string after the **toplevel**
  * A single space between the **prefix** and **@**
  * A single space between the **@** and the **domain**.
* If any of the above conditions occur, you should remove those spaces and
  evaluate the string as if the spaces did not exist, and if the remaining 
  string contains a valid e-mail, the function should return `True`.
* If there is more than one space either between the **prefix** and **@** or
  between the **@** and the **domain**, then the function should return `False`


**NOTE**: The above email name specifications are not the formal specifications
in actual use but are adapted for this assignment specifically.

### Approach
* Log into GitHub and visit the GitHub Classroom link provided in Sakai.  This
  will create a repository for your submission.
* Clone this repository to your local computer.
* Set-up GitHub Actions in this repository to implement CI testing.
* Develop code on feature branches.
* Write modular code.  So, have the `is_email` function call other functions
  if appropriate.
* Develop unit tests in parallel with code on feature branches.
* Ensure all functions and code, including the unit test functions, adhere to 
  PEP-8 style.
* Push code to GitHub.
* Generate Pull Request on GitHub.  Only merge your feature branches into the
  main branch once GitHub Actions reports a passing status (for both unit
  tests and PEP-8 style).
* Tag final submission on the main branch as `v1.0.0` or later number if 
    revisions are necessary.


### Grading Criteria
* Good git workflow usage (good commit messages and frequency, use of branches,
pull requests, etc.).
* Meeting the functional specifications above.
* Presence of comprehensive unit testing to ensure that the appropriate range 
of possible string inputs are checked.
* The use of `@pytest.mark.parametrize` for at least one unit test.
* Appropriate naming and syntax for unit tests and testing files.
* Implementation of GitHub Actions / CI Testing.
* Appropriate use of virtual environments.
* Code (functions and tests) meet PEP-8 style guidelines.
* Feature branches have passing GitHub Action tests (both unit tests and PEP-8
  style checks) before merging into main.
* Presence and content of README.md  (for this assignment, you do not need 
  to provide user instructions.  At a minimum, include author information and
  a brief description/purpose of the code)
