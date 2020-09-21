# Functional Decomposition
## Introduction
The goal of functional decomposition is to break down the program functionality
into  unit functions with specific and limited scope and follow the 
input->work->output paradigm.

We will demonstrate this in class by decomposing the following example.

## Example Program
#### Overview 
This program will read in an input file with various vital signs from a 
patient.  It will then scan these signs to determine which are within a normal
range and which are not.  It will then generate an output file that indicates
the condition of the patient.

#### Specifications
* Input file will be in the following format:
  ```
  HR=60
  BP=110/70
  O2=75
  Resp=15
  ```
  HR = Heart Rate, BP = Blood Pressure, O2 = oxygen saturation, Resp = 
  Respiratory rate
  
* If all vital signs are in a normal range, output file should be:
  ```
  Normal
  ```
* If any vital signs are not in a normal range, output file should say 
  `WARNING` and describe condition.  Example:
  ```
  WARNING:  O2=75 is abnormal
  ```

