# CPAP Data Analysis

## Background

Obstructive sleep apnea is a condition in which breathing stops involuntarily
for brief periods of time during sleep.  The flow of air stops because the
airways may constrict due to "floppy" muscles that do not keep the airways
open.  This disruption of airflow can lead to periods of decreased oxygen
supply to the brain and other parts of the body, as well as poor sleep quality
leading to daytime drowsiness.
(Source:  <https://www.healthline.com/health/sleep/obstructive-sleep-apnea>)

Obstructive sleep apnea is often treated with the use of a continuous positive
airway pressure (CPAP) machine.  The patient wears a mask connected to the
CPAP.  The mask provides pressurized air for the patient to breath.  The
pressure is set high enough to help keep open the airways so that they cannot
collapse and block air flow.  Breathing is not interrupted.

Most CPAPs collect some data during sleep.  This can include:
* the number of hours of use per night
* the amount of air leakage from the system (indicating poor mask fit)
* the number of "events per hour" in which the patient stops breathing for 10
seconds or more
  
During sleep studies, a pulse oximeter may also be used to continuously measure 
the oxygen saturation of the blood.

The data collected by the CPAP is then usually sent to a central server for
analysis and storage.

For this assignment, we will be writing some code that reads in CPAP data for
a variety of patients from an input file, analyzes these results, and then
creates separate output files for each patient.

## Input Data
A sample input file is found in a text file called `sample_data.txt` in this
repository.  The data for a single patient is found on five lines with the
following format:
```
FirstName LastName
Hours
Seal, s1, s2, s3, s4, etc.
Events, e1, e2, e3, e4, etc.
O2, o1, o2, o3, o4, etc.
```
The first line will have the first and last name of the patient separated by a
space.  
Example:  `Anne Boynton`

The second line will contain a decimal number indicating the number of hours
 of CPAP usage.  
Example:  `7.25`

The third line has the data for the air leakage or mask seal, in L/min, as 
decimal numbers. The line starts with
the label `Seal` to indicate its contents, then a comma, followed by hourly
average data for the seal separated by commas.  The number of hourly average
results will be the total hours of usage rounded down to the nearest hour. 
So, if the CPAP was used for 7.25 hours, there will be 7 values.  If the CPAP 
was used for 6.9 hrs, there will be 6 hours.  
Example:  `Seal, 11.0, 23.6, 15.2, 2.3, 4.0, 19.7, 3.7`

The fourth line has the data for the number of events per hour as integers.
The line starts with the
label `Events` to indicate its contents, then a comma, followed by the number
of events detected in each hour separated by commas.  There will be the same
number of values in this list as described above.  
Example:  `Events, 5, 0, 2, 3, 9, 1, 2`

The fifth line contains the data for the hourly average of the pulse oximeter 
readings in
percent as integers.  The line starts with the label `O2`, then a comma,
followed by a list of the hourly average pulse oximeter readings separated by
commas.  There will be the same number of values in this list as described
above.  
Example:  `O2, 95, 93, 98, 97, 96, 97, 100`

To clarify, the Seal, Event, and O2 list of results will all have the same
length for a particular patient.  But, the length of those lists may vary
from patient to patient based on their CPAP usage time.

In the `sample_data.txt` file, the first patient fills the first five rows,
the second patient fills the next five rows, etc.  After the last patient,
the file will have a line containing `END` to mark the end of the file.

## Program Specifications
* Read in the data from a text file.  `sample_data.txt` is a sample, but the 
  file on which your code will be graded will have different data and a 
  different number of patients.  So, your code must be flexible enough to 
  handle files with different number of patients.
* Calculate the average mask leakage for the night by averaging the given
  hourly values for "seal".
* Calculate the average events per hour for the night by averaging the given
  "event" totals per hour.
* From the results of the `Events` and `O2` data, assign one of the following
  diagnoses to the patient:
  + "normal sleep" if all O2 saturation values are 93 or higher and the average
    number of events per hour for the entire night is 5.0 or less
  + "hypoxia" if any of the O2 saturation values is below 93 and the average
    number of events per hour for the entire night is 5.0 or less
  + "apnea" if all O2 saturation values are 93 or higher and the average
    number of events per hour for the entire night is greater than 5.0 
  + "hypoxia apnea" if any of the O2 saturation values is below 93 and the 
    average number of events per hour for the entire night  is greater than 5.0
  This can be summarized in the following table:
  
  |  | All O2 values 93 and above | Any O2 value below 93
  | --- | --- | --- |
  | __Average Events <= 5.0__ | normal sleep | hypoxia |
  | __Average Events > 5.0__ | apnea | hypoxia apnea |

* For each patient, create an output file named "FirstName-LastName.json" where
  FirstName and LastName are replaced by the first name and last name of each
  patient.  Example:  `Anne-Boynton.json`.
* This output file should contain a dictionary in JSON format with the 
  following keys and corresponding values:
  + `First Name`, value is a string containing the patient's first name
  + `Last Name`, value is a string containing the patient's last name
  + `Hours`, value is a float containing the number of hours the CPAP was used
  + `Seal`, value is a list of floats containing all of the hourly seal values 
  + `Events`, value is a list of integers containing all of the hourly event 
    totals
  + `O2`, value is a list of integers containing of all of the hourly oxygen 
    saturation values
  + `Seal Average`, value is a float containing the average of the
    seal data for that patient
  + `Diagnosis`: value as a string containing one of the diagnoses listed above
* To create the above JSON output file, first create a dictionary with the keys
  listed exactly as above and assign each key the corresponding value.  Then, 
  using the `open` and `json` commands, create the file and output the 
  information.

### Notes
* In the dictionary description above, when a value is indicated to 
  be a float or integer, it should NOT be a string containing a float or 
  integer, but an actual number.
* Remember that when a line of text is read in by Python, it may have a return
character, `\n`, at the end which you will need to account for.  

  
## Grading Expectations
* Good git usage and workflow
* Meeting the above functional specifications
* Appropriate functional modularity that will allow for appropriate unit tests
* Unit testing exists for all functions that do any algorithmic work, excluding
input/output routines.
* GitHub Actions CI integration with all branches passing unit tests and PEP-8 
  style before merge
* Conforms to PEP-8 Style Guide 
* Docstrings exist for all functions
* Appropriate use of virtual environments as demonstrated by a
  `requirements.txt` and/or `environment.yml` file being present in your GitHub 
  repository.
* Presence and content of README.md
* Final submission is pushed to GitHub by the deadline and is tagged 
  appropriately.
* Plus any expectations from previous assignments

### Small Bonus
* Create `sphinx` documentation and push the resulting `*.html` files to your
GitHub repository.

  


