# Functional Decomposition
## Introduction
The goal of functional decomposition is to break down the program functionality
into  unit functions with specific and limited scope and follow the 
input->work->output paradigm.

We will demonstrate this in class by decomposing the following example.

## Example Program
#### Overview 
This program will read in an input file with hourly averages of CPAP data for
a patient.  The program will then analyze this data and output the results.

#### Specifications
* Example input file
  ```
  Anne Ables
  7.25  # hours of sleep
  Seal,11.0,23.6,15.2,2.3,4.0,19.7,3.7  # Hourly leakage
  Events,5,0,2,3,9,1,2  # Hourly apnea events
  O2,95,93,98,97,96,97,100  # Hourly O2 saturation
  ```
  
* Example output file
  ```
  {
    "First Name": "Anne",
    "Last Name": "Ables",
    "Hours": 7.25,
    "Seal_Ave": 11.36,
    "Events_Ave": 3.14,
    "O2_Min": 93,
    "Diagnosis": "normal sleep"
  }
  ```
* __Diagnosis__

  |  | All O2 values 93 and above | Any O2 value below 93
  | --- | --- | --- |
  | __Average Events <= 5.0__ | normal sleep | hypoxia |
  | __Average Events > 5.0__ | apnea | hypoxia apnea |


