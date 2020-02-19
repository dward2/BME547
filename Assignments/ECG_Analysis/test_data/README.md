This README details the information for the tests csv files in this folder and
the source of the data.

## Source
This data is originally from the [PhysioBank
Database](https://physionet.org/physiobank/database/#ecg) for ECG data.

## Test Files Description
* The data are given as `time, voltage` pairs.  `time` is in seconds, `voltage`
is in mV.
* **Tests 1-27** include variable forms of ECG data. Some files have peaks at a
constant voltage and period, while others have peaks at different voltages and
a change in heart rate within the data set. The time intervals between
measurements may vary per data set.

* **Tests 28-31** contain some non-numeric entries, missing data, or NaN in 
the time and voltage columns.  
  - When NaN exists in the CSV file, and it is converted from a string to
    a float in Python, Python will not raise an error, but the float variable
    will be given the special identifier `nan` which means "not a number" to 
    Python.  To detect the presence of the `nan` identifier in a float 
    variable, use the function `math.isnan()` which will return `True` if 
    `nan`, `False` otherwise.
      
 * **Test 32** has values outside of the normal range of ECG data at a max of 
 +/- 300 mV. Test if program can detect these values are outside of ECG range.
