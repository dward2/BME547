This README details the information for the tests csv files in this folder and
the source of the data.

## Source
This data is originally from the [PhysioBank
Database](https://physionet.org/physiobank/database/#ecg) for ECG data.

## Test Files Description
* **Tests 1-27** include variable forms of ECG data. Some files have peaks at a
constant voltage and period, while others have peaks at different voltages and
a change in heart rate within the data set. The time intervals between
measurements are vary per data set.

* **Tests 28-30** test inputs that have strings and missing data in the time and
voltage columns.

* **Test 31** has sparse gaps in the time domain. Test will determine how code
handles smaller gaps in time and tests if time data can/is interpolated in
these cases.

 * **Test 32** has values outside of the normal range of ECG data at a max of ~300
mV. Test if program can detect these values are outside of ECG range.
