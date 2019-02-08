# Dictionary and JSON Assignment

## Set-up
Hypothroidism and hyperthyroidism are conditions where the thyroid gland 
produces either too little (hypo) or too much (hyper) of the hormone thyroxine.

The thyroid gland is under the control of the pituitary gland.  When the level
of thyroxine drops too low, the pituitary gland produces Thyroid Stimulating
Hormone (TSH) which stimulates the thyroid gland to produce more hormones.
If the thyroid produces too little thyroxine, the amount of TSH produced by
the pituitary gland is very high.  If the thyroid produces too much
thyroxine, the pituitary gland produces very little TSH.  Therefore, TSH levels
are often used to diagnose thyroid gland issues.  

For this assignment, we will be writing some code that is reading in patient
data containing TSH test results.  This data will be analyzed for hypothyroidism
and hyperthyroidism and then stored in a JSON output file.

## Input Data
The input data is found in a text file called `test_data.txt` found in this 
repository.  The data for a single patient is found on four lines with the 
following format:
```
FirstName LastName
Age
Gender
TSH, result1, result2, result3, etc.
```
The first line will have the first and last name of the patient separated 
by a space.  
The second line will contain the age of the patient.  
The third line will contain the gender of the patient.  
The fourth line contains the name of test, followed by a comma, and then a
list of test results separated by commas.  The number of test results will
vary from patient to patient.

In the `test_data.txt` file, the first patient fills the first four rows, the
second patient fills the next four rows, etc.  After the last patient, the
file will have a line containing `END` to mark the end of the file.

## Program Specifications
* Read in the data from this text file.
* From the TSH results from each patient, diagnose whether the patient has:
  + "hyperthyroidism" as defined by any of their tests results being less than 1.0,
  + "hypothyroidism" as defined by any of their test results being greater than 4.0, or
  + "normal thyroid function" as defined by all of their test results being
  between 1.0 and 4.0, inclusive.
  + No single patient will have test results both above 4.0 and below 1.0,
  hence will only meet one of the diagnoses above.
* For each patient, create an output file named "FirstName-LastName.json".
The file should contain the following information in JSON format: 
  + First Name
  + Last Name
  + Age
  + Gender
  + Diagnosis
  + TSH (containing a list of all of the test results)
* To create the above JSON output file, first create a dictionary with the keys
listed above and their corresponding values.  Then, using the `open` and `json`
commands, create and output the information.


## Grading Expectations
* Good git usage and workflow
* Meeting the above functional specifications
* Appropriate functional modularity
* Unit testing exists for your function(s) that determine the diagnosis, 
following appropriate nomenclature and comprehensiveness.
(For this assignment, unit tests are not required for input/output routines, or
string handling, unless you find them useful)
* Travis CI integration
* Conforms to PEP-8 Style Guide 
* Docstrings exist for all functions
* Appropriate use of virtual environments, including a `requirements.txt` or 
`environment.yml` file being present in your GitHub repository.
* Presence and content of README.md
* Final submission is pushed to GitHub by deadline and is tagged appropriately.

### Bonus
* Sort the list of TSH values (low to high) before outputing them to the JSON
file. 
*  Create `sphinx` documentation and push the resulting `*.html` files to your
GitHub repository.
