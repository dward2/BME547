# Final Project Add On

Develop a GUI that displays the names of all available patients and 
their most recent heart rate (if one exists).  The GUI should automatically
update (at least once every 30 seconds) with any new patients that are
added to the database and any updated heart rates for existing patients.

For each patient on the GUI, there must be some clickable object associated
with that patient that will cause the display to show the most recent
ECG trace for that patient.  The clickable object could be the patient
name, the patient heart rate, or a button or other widget associated with
each patient.  So, for example, if there are five patients in the 
database, there should be five separate clickable widgets that would each
display the ECG trace for a specific patient.  

While the ECG trace is being displayed, if the heart rate for that particular
patient is updated in the database, the displayed ECG image should also 
update with the new data.

While the ECG trace is being displayed, there should be a button or some other 
way for the user to say they are done looking at the ECG trace and have it
be removed and show all of the patients again.