# Sleep Lab Monitoring Client/Server Project

## Overview
The final project in this class will require you to leverage the
industry-standard skills you've learned during this semester to design
and implement a Sleep Lab Monitoring
System that has a patient-side client, a monitoring-station client, and a
server/database that allows patient data to be uploaded and stored on the
server, retrieved for ad-hoc and continuous monitoring, and for communication
of updated settings to the patient.

It is expected that you will follow proper professional software
development and design conventions taught in this class, including:
* git feature-branch workflow
* continuous integration
* unit testing
* PEP8
* docstrings
* use of issues and milestones to track development progress (new to this 
assignment)
  
## Functional Specifications
### Patient-side GUI Client
The patient-side GUI will act as a stand-in for a CPAP machine which is 
tracking a particular patient undergoing a sleep study.

At a minimum, your patient-side GUI client should provide a __graphical__ user 
interface with the following functionality:
  + Allow the user to enter a patient name.
  + Allow the user to enter a patient medical record number (MRN).
  + Allow the user to enter a room number.
  + Allow the user to enter a CPAP pressure in units of cmH2O (the GUI should validate
    that the entry is an integer and must be between 4 and 25, inclusive, which 
    is the typical range for CPAP operation).
  + Allow the user to select a CPAP data file from the local computer.  This
  CPAP data should then be analyzed for:
    + breathing rate in breaths per minute, 
    + number of apnea events
    + flow rate vs. time
  + The resulting breathing rate and number of apnea events should be displayed 
  in the GUI along with an image of the flow rate vs. time curve.  The
  combination of breathing rate, number of apnea events, and the CPAP flow
  image will be referred to as the CPAP calculated data.
  + If the number of apnea events is two or greater, that value should be 
  displayed in red.  If it zero or one, it should be displayed in the default color of the
  rest of the text in the GUI.
  + Upon user command, issue a RESTful API request to your server to upload
  whatever information is entered above.  The interface should only allow this
  request to be made if at least a medical record number and a room number have 
  been entered.  This upload should include:
    + the patient medical record number
    + the patient room number
    + if entered, the patient name
    + if both a CPAP pressure and CPAP calculated data have been entered, 
      upload the CPAP pressure, breathing rate, apnea count, and CPAP flow
      image (the flow vs time data does not need to be uploaded, just the plot)
  + After the initial upload, the medical record number and room number entry
  should be locked out/deactivated so that no further changes can be made to 
  them (until the condition described below).  Note, the values for MRN and 
  room number should still be visible in the GUI.  
  + After upload, the information entered in the GUI should REMAIN in the GUI 
  so it can still be seen.  
  + The user should have the ability to update the patient name, change the CPAP
  pressure, and select a
  new CPAP data file for analysis and then send these updates to the server
  upon command.  The MRN and room number should not change. If the patient name 
  is updated in the GUI, it should be replaced in the server.  If the CPAP pressure/
  breathing
  rate/apnea count/CPAP flow image is updated in the GUI, this new information
  should be added to the existing information on the server.  (In other words,
  there can be multiple CPAP calculated data measurements in the database for a patient.)
  + The GUI should periodically (at least every 30 seconds, but can be more 
  frequent) query the server
  to see if a new CPAP pressure has been commanded by the monitoring station.
  If so, the value in the CPAP pressure entry should be automatically updated
  to that new value.  Any future uploads of CPAP data should use this new
  value.
  + The user should have the ability to "reset" the device.  This means that
  all entries and displayed data are removed, including the patient medical 
  record number and room number.  The MRN and room number inputs should be 
  reactivated so that the GUI could be used for a new patient.  Any data 
  about the previous patient should be removed so it is not accidentally 
  uploaded with any new patient information.

For the analysis of CPAP data, please use your existing CPAP Measurements 
code module, and modify it with a function that your GUI can call to execute
your code to do the analysis and return it.  The CPAP data files will follow
the same format as those from the CPAP Measurement assignment.  (In fact, they
will basically be the same files, but I will modify them to remove any missing
data so that there are no problems with that and I may also increase the number
of apnea events.)  This CPAP Measurement code will not be re-evaluated and does 
not need unit tests (although it will still need to pass PEP-8 testing).  The 
only evaluation that will be made is that you call the interface function 
correctly from the GUI code and receive the needed CPAP data back.  You will 
need to get the flow vs. time data in order to create the plot.  You do not 
need to correct your CPAP measurements.  Whatever results your code currently
returns will be considered the correct values for this assignment.  
   
### Monitoring-Station GUI Client
The monitoring-station GUI will be considered a stand-in for a central 
monitoring location where the sleep lab technicians can monitor the CPAP 
results for all patients and command changes in the CPAP pressure for specific
patients/rooms.

At a minimum, your monitoring-station GUI client should provide a __graphical__
user interface with the following functionality:
  + Allow the user to select a room number from a list of available numbers on 
  the server.
  + For the selected room number, display the medical record number, the patient
  name, the latest CPAP pressure and breathing rate/apnea count/CPAP flow image 
  (if they exist), and 
  the date/time at which this latest CPAP calculated data was uploaded to the server.
  + The information displayed should be from the most recent patient in the 
  room.
  + If the apnea count value is two or greater, it should be displayed in red.
    If it is zero or one, it should be displayed in the default text color used
    by the rest of the GUI.
  + Allow the user to select from a list of the date/times of all stored CPAP calculated
    data for the selected patient, download the appropriate CPAP flow image, and 
    display the selected image side-by-side with the latest CPAP flow image already 
    displayed.
  + Allow the user to save a downloaded and displayed CPAP flow image (either the latest or the
    historical one chosen) to a file on their local computer.
  + Allow the user to enter an updated CPAP pressure and upload this new
    pressure to the server to be retrieved by the patient-side GUI.  The GUI
    should only allow integer values of 4 to 25, inclusive, to be entered and uploaded.
  + When the user selects a new room, any information from the previous
  patient on the interface needs to be replaced with the information from the
  new room/patient or removed from the interface.
  + The interface should make periodic requests (at least every 30 seconds, but
  can be more frequent) to the server to check for any updated information for
  the currently selected room.  If new CPAP data is 
  available, those should be automatically downloaded and displayed on the 
  interface in place of the old data.
  + When the user wants to select a new room or historical CPAP calculated data, the 
   choices presented should represent the 
    most recent options on the server.  In other words, the options for choices
    must dynamically update, rather than be "locked in" based on what was 
    available when the client was started.  
  + In order to complete these tasks, the client GUI will need to make RESTful 
  API requests to the server to get lists of available room
  numbers, available data for the selected room, and the data/images 
  themselves, as well as send updates to the CPAP pressure.

### Cloud Server
At a minimum, your server should be a cloud-based web service running on your 
virtual machine that exposes a well-crafted RESTful API that will implement 
the tasks needed by the clients as described above and outlined here:

* Accept uploads from the patient-side client that will include, at a minimum,
the room number and medical record number.  The upload may also include a 
patient name, CPAP pressure, and CPAP calculated data/image.
* Communicate with and utilize a persistent database that will store the above
uploaded data for retrieval at a future time.  
* When CPAP calculated data are received, the date and time of receipt 
should be stored with the data.
* If the upload contains a room and/or medical record number not already found in the 
database, a new entry should be made for that room and/or patient, and the information 
  sent with the request stored in this new record.  
* If the upload contains a medical record number already found in the database,
the CPAP calculated data sent with the request should be
added to the existing information. If a patient name is also sent, it should 
update the existing name in the database.
* Accept requests from the monitoring-station client to retrieve the following
information from the database and download it to the client:
  + a list of available room numbers
  + the name and medical record number of the latest patient in a specific room
  + the latest CPAP pressure and CPAP data for the latest patient in a specific
    room
  + a list of CPAP calculated data timestamps for the latest patient in a specific room
  + a specific CPAP image based on timestamp for the latest patient in a specific
    room 

  __Note__: The above list does not imply that you must have one route for
  each of those items.  Just make sure your server provides the needed 
  services.
* Accepts requests from the monitoring station client with updated CPAP
pressure information for a specific room.
* Accepts requests from the patient-side client for updated CPAP pressure for
a specific room (note, it may not exist if no new pressure has been given by
the monitoring station)
* Provide any other services as needed for either client to perform its needed
functions.

**Note**: The GUIs should only make requests to the server and should not make 
contact with the database.  All database functions should be handled from the
server.  If the GUI needs to interact with the database, it should do it by
making requests of the server. 

### Multiple Patient-side Clients
The system should allow for multiple patient-side GUIs to be running 
simultaneously to simulate a sleep lab where multiple CPAPs are reporting to
a central monitoring station.  In theory, you should not need to make any
coding adjustments based on whether there is only a single patient-side client
running or multiple patient-side clients running.  I will be
testing your final submission by opening up multiple patient-side GUIs and a 
single monitoring station GUI and using all at the same time.  You may want to
test your system that way at least once.

## Choice of GUI Framework
`tkinter` can provide all of the GUI functionality necessary to meet the
above objectives.  However, you are also welcome to use a different GUI
framework if you like, such as PyQT or any other choice.  You are also welcome
to program a web/browser GUI for your clients if you prefer.  Visit
<https://github.com/dward2/BME547/tree/main/Resources/WebInterface> for info
and basic tutorials for using HTML/CSS/flask to create such an interface.

## Database
As discussed in class, using MongoDB and PyModm will satisfy the requirements
for a persistent database.  As all team members will be working with the 
database, the use of any other type of persistent data base (SQL instead of
non-relational, or a non-MongoDB online option) requires approval from all
team members and the instructor.

## Planning
* It is a requirement for this assignment you develop milestones and issues
  that provide a detailed plan of how you will approach and implement this
  project.
* Add these milestones and issues to your GitHub repository.
* Each issue should be assigned to a team member.  
* One team member must be responsible for coding the patient-side GUI.  The
  other team member must be responsible for coding the monitoring-side GUI.
  Make sure the issues above make it clear which team member is responsible
  for which GUI.
* All other issues can be assigned to either team member with the goal of
  balancing work load among the members.  Both team members may work
  on any specific issue, but the assigned team member should make sure that 
  the issue is addressed/implemented.
* It is suggested that your database-related issues describe, as best as possible, the
  database structure desired.
* Notify the instructor when your plan is available for review before you begin
  significant coding activities.

## Deliverables
* All project code for the two GUI clients, server, and tests (in the form of a 
  tagged GitHub repository).  All code should be well documented with docstrings.
* A detailed `README` describing the final performance and state of your
  project.  This should include a basic instruction manual for your GUI 
  clients, an API reference guide for your server, and a description of your
  database structure.
* Recorded video demo of your client programs in action.      
* The URL of your deployed web service in your`README.md` (e.g., 
  `vcm-11111.vm.duke.edu:5000`)

#### Video demo
* This can be a recorded screen capture or a video taken by camera.
* Zoom allows an easy way to record actions on your screen with narration.
Visit <https://support.zoom.us/hc/en-us/articles/201362473-Local-Recording> or
do a web search on "using zoom to record screen" for lots of tutorials.
* The video can be shared in many ways: a link to your cloud Zoom recording, on 
YouTube, Duke Box, or any other method.  While it is possible that you could
commit your video to your GitHub repository, the "free" storage limits on 
GitHub can be reached pretty quickly with video.  So, please use this as a last
resort.  Indicate in your `README.md` how I can access the video.

<!--## Recommended Datasets
Your project may utilize some existing databases of images (or you can choose to
use your own images).  Here are some example datasets that you can access for
this project:

* <https://medpix.nlm.nih.gov/home>
* http://www.vision.caltech.edu/Image_Datasets/Caltech101/
* <https://www.cs.toronto.edu/~kriz/cifar.html>
* https://github.com/beamandrew/medical-data
* Over 13000 annotated skin lesion images are available from the International
  Skin Imaging Collaboration (ISIC) project:
  https://isic-archive.com. 
-->
## Grading

The following is a partial list of aspects on which the project that will be 
graded.

* Git Repository
  + Issues/Milestones (New for this assignment)
  + Commits are discrete, logical changesets
  + Feature-branch workflow
* Software best practices
  + Modularity of software code
  + Handling and raising exceptions
  + Language convention and style (PEP8)
  + Docstrings for all functions
* Testing and CI
  + Unit test coverage of all functions (except Flask handler and GUI calls)
  + Travis CI passing build
* Cloud-based Web Service
  + RESTful API Design 
  + Validation Logic 
  + Returning proper error codes
  + Robust deployment on virtual machine 
* Proper use of a database 
* User interface functionality
* Demo of the final working project
* Robust README

## Links of Interest
* [Image Toolbox](../Resources/image_toolbox.md)
* [Tkinter Intro](../Lectures/intro_to_gui.md)
* [Images in Tkinter](../Resources/tkinter_images.md)
* [Tkinter Toolbox](../Resources/tkinter_toolbox.md) 

## Q & A and Clarifications
As questions are raised and clarifications made, I will include those here:

**Testing of Image Toolbox Code**

Question: Does the "image toolbox" code that I shared need to be tested with unit 
tests.  The answer is **yes**.  Ideally, 
all of your code will have a unit test.  As we have seen so far this semester, 
some code can be problematic to have a unit test for (such as the flask 
handlers or GUI code).  But, this image code can be tested.

I have added some sample tests and advice on how to devise such tests on the 
class GitHub repo page [Resources/image_toolbox.md](https://github.com/dward2/BME547/blob/master/Resources/image_toolbox.md#testing-toolbox-code).

Please, if you are having any trouble designing a unit test for any of your 
functions, please open a GitHub issue with a link to the function you are 
trying to test and I will help you design an appropriate test.  And, if you 
have any question about the information on this webpage, please let me know.

