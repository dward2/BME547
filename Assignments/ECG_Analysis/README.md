# ECG Analysis Assignment

* GitHub Classroom will be used to host repositories.  Travis-CI integration 
with the BME547-Spring2019 organization has been established.  
* After signing into GitHub, visit the GitHub Classroom link found in Sakai.
  A private repository will be created in the BME547-Spring2019 organization
  for you to use.  The repository will be pre-populated with the ECG test data
  needed for the assignment.  Once a `.travis.yml` file is correctly created, 
  Travis-CI integration will be made with your repository.

## ECG Analysis: Functional Specifications
  + Read ECG data from a CSV file that will have lines with `time, voltage`. 
  Example data can be found in the `test_data/` directory in this assignment directory.  
  + The following data should be calculated and saved as keys in a Python 
  dictionary called `metrics`:
    - `duration`: time duration of the ECG strip  
    - `voltage_extremes`: tuple containing minimum and maximum lead voltages  
    - `num_beats`: number of detected beats in the strip
    - `mean_hr_bpm`: estimated average heart rate over the length of the strip  
    - `beats`: numpy array of times when a beat occurred
  + Your `metrics` dictionary should be output as a [JSON](https://json.org/) 
  file.  The json file should have the same name as the ECG data file, but
   with an extension of `.json`.  Example:  the dictionary 
  with results from the ECG data found in `test_data12.csv` should be saved in
  a json file called `test_data12.json`.   

## Git Version Control Expectations
* Frequent and meaningful commits!
* Branches should be used for specific feature implementions, bug fixes, etc.
* Merge your feature branches into the master branch using Pull Requests
  on Git Hub.
  - Feature branches should be merged after passing unit tests with Travis CI.
  - Do not delete your branches after merging them into master.
* Create an annotated tag titled `v1.0.0` or subsequent version when your
    assignment is completed and ready to be graded.
* Make sure that your project has a `README.md` file that contains:
  - instructions on how to run your program
  - how you are calculating the beats per minute once you have identified
        the beats
  - a software license with your project (http://choosealicense.com/)  
  - anything else you think the graders should know to understand the operation
      and function of your code.
* Bonus - integrate a Travis [status badge](https://docs.travis-ci.com/user/status-images/) 
        in your README that displays the status of test passage
  

## Python Code Expectations
* Modular code:  write a single function for each functional element of your 
    code, and all functions must have associated unit tests with comprehensive 
    coverage.
* Utilize a virtual environment.
* Have Sphinx-friendly docstrings for all methods.  
* Unit tests should exist in a separate file or directory of test files using
    standard naming conventions. 
* Achieve the functional specifications with passing unit tests.  Make sure 
    that you include a test for writing the output JSON file.
* All methods should have well-defined input-action-output (as the unit tests 
    will demand).
* There should be no "hard-coded" values in your methods.
* Adhere to [PEP8](https://www.python.org/dev/peps/pep-0008/) style. 
* Implement exception handling: when reading in ECG data, if a non-numeric
    value is encountered, an exception should be raised and handled by the 
    calling function with a try/except
* Gracefully terminate when the input file ends
* Create meaningful logs  
   - log as `INFO` when starting analysis of a new ECG trace
   - log as `INFO` when assigning/calculating an attribute/dictionary entry
   - log as `WARNING` or `ERROR` when exceptions are generated

## Grading Criteria
* Meeting the expectations outlined above, including...
* Effective version control usage
* Adequate unit test coverage and functional modularity
* Python style and docstrings
* Achieves functional specifications
* Works with all of the provided test data
