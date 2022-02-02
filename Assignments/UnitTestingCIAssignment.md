# Unit Testing and Continuous Integration

In this assignment, you will write a function and comprehensive unit tests to
ensure the function meets specifications.  You will also configure Continuous
Integration (CI) to automatically run tests on push and pull request events.

See Sakai for GitHub Classroom link and due date.

### Background
With the transition towards electronic medical records, many paper records are
being scanned into a digital format.  [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition)
(OCR) is used so that the scanned text is searchable.  Depending on the 
quality of the paper records (often derived from faxes), the quality of the 
OCR result may not be perfect.  Therefore, any code that is looking to 
interpret the scanned results needs to be flexible enough to read results that
may be slightly off.  This assignment simulates a small example of such a
problem.  

Tachycardia is a heart rate that exceeds the normal resting heart rate.  In
this assignment, you will be writing a function that could be used to
interpret whether a string obtained from OCR of medical records contains the 
word "tachycardic". 

### Function Specifications
* Should be named `is_tachycardic` and located in a module called 
`tachycardia.py`.
* It should receive a parameter containing the string to check.
* This string will only contain a single word, but there is no guarantee
whether the word will be upper case, lower case, mixed case, and/or have one or 
  more leading /trailing spaces and/or one or more punctuation marks.  
* If the string contains the word "tachycardic," regardless of capitalization
and leading or trailing spaces or punctuation, the function should return a 
boolean value of `True`.
* Otherwise, the function should return a boolean value of `False`.

### Approach
* Log into GitHub and visit the GitHub Classroom link provided in Sakai.  This
  will create a repository for your submission.
* Clone this repository to your local computer.
* Set-up GitHub Actions in this repository to implement CI testing.
* Develop code on feature branches.
* Develop appropriate unit tests in parallel with code on feature branches.
* Ensure all functions and code, including the unit test functions, adhere to 
  PEP-8 style.
* Push code to GitHub.
* Generate Pull Request on GitHub.  Only merge your feature branches into the
  main branch once GitHub Actions reports a passing status.
* Tag final submission on the main branch as `v1.0.0` or later number if 
    revisions are necessary.


### Grading Criteria
* Good git workflow usage (good commit messages and frequency, use of branches,
pull requests, etc.).
* Meeting the functional specifications above.
* Presence of comprehensive unit testing to ensure that the appropriate range 
of possible string inputs are successfully identified or rejected.
* The use of `@pytest.mark.parametrize` for at least one unit test.
* Appropriate naming and syntax for unit tests and testing files.
* Implementation of GitHub Actions / CI Testing.
* Appropriate use of virtual environments.
* Code (functions and tests) meet PEP-8 style guidelines.
* Presence and content of README.md

### Small Bonus:
Make your `is_tachycardic` function more tolerant to close representations of
the word `tachycardic`.  For example, it should be able to tolerate 1 to 2
missing letters (ex. `tachycrdic`) and/or 1 to 2 misspelled letters
(ex. `tachycard1c` where the `i` is replaced with `1`).
