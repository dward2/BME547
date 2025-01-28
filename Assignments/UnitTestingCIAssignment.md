# Unit Testing and Continuous Integration

In this assignment, you will write a function and comprehensive unit tests to
ensure the function meets specifications. You will also configure Continuous
Integration (CI) to automatically run tests on pull requests in GitHub.

See Canvas for due date and information about setting up a repository for the
assignment.

### Background

Assume you are part of a research team that works on protein synthesis and RNA
sequencing. Old paper results containing various RNA sequences have been
scanned into a file. The optical character recognition used to determine the
RNA sequences on paper sometimes makes mistakes:  spaces are mistakenly added,
G's are recognized as O's, or other letters may be misidentified. You have been
tasked to write a Python function that analyzes the scanned text and determine
whether it contains a valid RNA sequence. As described above, the quality of
the character recognition may not be perfect. Therefore, your code needs to be
flexible enough to read and accept results that may be slightly off.

RNA sequences describe the series of amino acids that are combined to make
various proteins. An RNA sequence is made up multiple codons where a codon is a
set of three RNA bases. The possible RNA bases are Uracil (U), cytosine (C),
adenine (A), and guanine (G). A codon is generally indicated by three letters.
Examples:  CAG, UUA. The RNA sequence is then these codons listed out. An
example:  AUGACAUGCUCCCAUUAA. The sequence must start with one of three "start"
codons and end with one of three "stop" codons.

### Function Specifications

* The function should be named `is_sequence` and located in a module called
  `rna_sequence_checker.py`.
* The function should receive a single parameter containing the string to
  check.
* The function should return a boolean value.
  * The boolean value should be `True` if the string sent to the function 
    contains a valid RNA sequence.
  * The boolean value should be `False` if the string does not contain a 
    valid RNA sequence.
* The following statements can be used to determine whether the input string 
  parameter contains an valid RNA sequence.
  * If the string contains two or more adjacent spaces anywhere between 
    letters, it is NOT an acceptable sequence.  Single spaces between 
    letters can be ignored.
  * It can have any number of leading or trailing spaces, which should be 
    ignored.
  * If any two or more adjacent letters consists of letters other than U, C, A,
    G, or O, it is not a valid sequence.
  * Any single letter that is not a U, C, A, G, or O can be ignored.
  * The number of remaining letters (those that are not ignored) must be a
    multiple of three. If it is not a multiple of 3, it is not a valid sequence.
  * Starting from the beginning of the remaining letters, each group of 
    three letters is a codon.
  * If a codon has a single O, it is considered an improperly scanned G and 
    should be treated the same as a G.  But, if a codon has two or more Os, 
    it is not considered a proper codon and the string does NOT contain a valid
    sequence.
  * The first codon must a "start" codon.  Start codons are:
    * UUG
    * AUG
    * GUG
  * The final codon must be a "stop" codon.  Stop codons are:
    * UAA
    * UAG
    * UGA
  * If the first codon is not a "start" codon or the final codon is not a 
    "stop" codon, then the string does NOT contain a valid sequence.
  * If a start codon is found anywhere but at the start of the sequence, or 
    a stop codon is found anywhere but at the end of the sequence, it is 
    NOT a valid sequence.
  * If there are three or more adjacent codons that are identical, it is 
    not a valid sequence.

**NOTE**: While most of the description above does apply to true RNA sequences,
some are simplified or modified for use in this assignment.

**NOTE**: You cannot assume that the string sent to your function will always
have any content.

**NOTE**: You are NOT allowed to use any existing third-party code, package,
or software that analyzes RNA sequences as part of your submission.

### Approach

* Log into GitHub and visit the GitHub repository created for you.
* Clone this repository to your local computer.
* Set-up GitHub Actions in this repository to implement CI testing 
  (suggested approaches for doing this can be found [here](../Lectures/continuous_integration_github_actions.md#recommended-workflows-for-setting-up-github-actions-and-other-repository-items).
* Develop code (including test functions) on feature branches.
* Consider using test-driven development (TDD) and write a unit test for the
  `is_sequence` function with appropriate test cases before you start writing
  the `is_sequence` code. This will give you a target for correct answers for
  your function.
* Write modular code. So, have the `is_sequence` function call other 
  helper functions when appropriate.
* For code written on a feature branch, develop unit tests for that code on the
  same branch before merging.  You will need to write unit tests for each 
  helper function even though the `is_sequence` will also have unit tests.
* Ensure all functions and code, including the unit test functions, adhere to
  PEP-8 style.
* Push code to GitHub.
* Generate Pull Request on GitHub. Only merge your feature branches into the
  main branch once GitHub Actions reports a passing status (for both unit tests
  and PEP-8 style) and that all functions being merged have appropriate test
  coverage.
* Tag final submission on the main branch as `v1.0.0` or later number if
  revisions are necessary.

### Grading Criteria

* Good git workflow usage (good commit messages and frequency, use of branches,
  pull requests, creating branches from latest, merged main branch, etc.).
* Meeting the functional specifications above.
* Presence of comprehensive unit testing to ensure that the appropriate range
  of possible string inputs are checked and that all functional 
  specifications are correctly met.
* The use of `@pytest.mark.parametrize` for at least one unit test.
* Appropriate naming and syntax for unit tests and testing modules.
* Implementation of GitHub Actions / CI Testing.
* Appropriate use of virtual environments.
* Code (functions and tests) meet PEP-8 style guidelines.
* Feature branches have passing GitHub Action tests (both unit tests and PEP-8
  style checks) before merging into main.
* Presence and content of README.md  (for this assignment, you do not need to
  provide user instructions. At a minimum, include author information and a
  brief description/purpose of the code)
