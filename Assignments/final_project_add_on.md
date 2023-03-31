# Final Project Add On

Develop a GUI that allows a user to see, in a single display, all of the
available room numbers and the information on the patient in each room
simultaneously.  For example, if there are four rooms currently registered
with the server, the display should have four sections, each of which shows
information about the patient in that room.

For each room, the display should include the room number, patient medical 
record number, and (if they exist) patient name, latest CPAP pressure, latest
breathing rate, and latest apnea count.  If the apnea count is two or greater,
it should be displayed in red.  Otherwise, it should match the default text
color used by the rest of the GUI.  For each room, the GUI should also
display the total apnea count for all data for the latest patient.  So, for
example, assume a patient exists in the database with the following apnea count data:

| Time | Apnea Count |
| --- | --- |
| 1/1/23 01:00:00 | 2 |
| 1/1/23 02:00:00 | 0 |
| 1/1/23 03:00:00 | 1 |

The GUI should display the latest apnea count as `1` and the total apnea
count as `3`.


The GUI should automatically update (at least once every 30 seconds) with any 
new rooms that are added to the database and any updates for any existing
rooms (i.e., new names, new breathing rates/apnea counts, etc.).

For each room on the GUI, there must be some clickable object associated
with that patient that will cause the display to show the most recent
CPAP flow image for that patient.  The clickable object could be the room
number, any other information associated with that room, or a button or other 
widget associated with each room.  So, for example, if there are five patients in the 
database, there should be five separate clickable widgets that would each 
display the latest CPAP flow image for the appropriate patient.  

While the CPAP flow image is being displayed, if the CPAP flow image for that 
particular patient is updated in the database, the displayed CPAP flow image 
should also update with the new data.

While the CPAP flow image is being displayed, the user should be able to see or
access a list of all the available historic timestamps for CPAP data 
for the latest patient in the selected room.  The user should be able to select 
one of those
timestamps and show the CPAP flow image associated with that timestamp next to the
already displayed most recent CPAP flow image.

While the CPAP flow image is being displayed, there should be a button or some other 
way for the user to say they are done looking at the image and have it
be removed and show all of the patients again.  If a second CPAP flow image was 
loaded for comparison, it should also be removed.

The GUI should allow the user to send an updated CPAP pressure for any specific 
room to the server to be retrieved by the patient-side client.  How this is
done is a design-decision for the developer.

