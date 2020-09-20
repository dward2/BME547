This README details the information for the test csv files which will be found 
in this folder of the GitHub Classroom repository that will be created for
your use in this assignment.

## Source
This data is originally from the [PhysioBank
Database](https://physionet.org/physiobank/database/#ecg) for ECG data, with
some modifications.

## Test Files Description
* The data are given as `time, voltage` pairs.  `time` is in seconds, `voltage`
is in mV.
* These files include variable forms of ECG data. Some files have peaks at a
constant voltage and period, while others have peaks at different voltages and
a change in heart rate within the data set. The time intervals between
measurements may vary per data set.
* Some data sets have been corrupted with additional low (<1 Hz) and/or 
high (>50 Hz)) frequency noise.
* For your assistance in developing appropriate data screening and
noise reduction, the `test_data1_orig.csv` found in this folder is
the raw data before the various additional signals were added.  You
can use this data to check the results of your data cleaning.  Note,
do not expect to get a perfect match to this data.  Just make sure
that you can clean-up the data well enough to observe and detect
the peaks.  

* **Tests 11, 20, 28, and 31** contain some non-numeric entries, missing data, 
or NaN in the time and voltage columns.   
  - When NaN exists in the CSV file, and it is converted from a string to
    a float in Python, Python will not raise an error, but the float variable
    will be given the special identifier `nan` which means "not a number" to 
    Python.  To detect the presence of the `nan` identifier in a float 
    variable, use the function `math.isnan()` which will return `True` if 
    `nan`, `False` otherwise.
      
 * **Test 32** has values outside of the normal range of ECG data at a max of 
 +/- 300 mV. Test if program can detect these values are outside of ECG range.
