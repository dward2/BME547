# Sleep Lab Monitoring Client/Server Project<br>Final Project for One Person (Spring 2023)

## Overview
The final project in this class will require you to leverage the
industry-standard skills you've learned during this semester to design
and implement a Sleep Lab Monitoring
System that has a patient-side client and a
server/database that allows patient data to be uploaded and stored on the
server for later ad-hoc and continuous monitoring.

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
* Provide any other services as needed for the client to perform its needed
functions.

**Note**: The GUI should only make requests to the server and should not make 
contact with the database.  All database functions should be handled from the
server.  If the GUI needs to interact with the database, it should do it by
making requests of the server. 

## Choice of GUI Framework
`tkinter` can provide all of the GUI functionality necessary to meet the
above objectives.  However, you are also welcome to use a different GUI
framework if you like, such as PyQT or any other choice.  You are also welcome
to program a web/browser GUI for your clients if you prefer.  Visit
<https://github.com/dward2/BME547/tree/main/Resources/WebInterface> for info
and basic tutorials for using HTML/CSS/flask to create such an interface.

## Database
As discussed in class, using MongoDB and PyModm will satisfy the requirements
for a persistent database.  If desired, an alternative database may be used if
permission is received from the instructor ahead of time.

## Planning
* It is a requirement for this assignment you develop milestones and issues
  that provide a detailed plan of how you will approach and implement this
  project.
* Add these milestones and issues to your GitHub repository.
* It is suggested that your database-related issues describe, as best as possible, the
  database structure desired.
* Notify the instructor when your plan is available for review before you begin
  significant coding activities.

## Deliverables
* All project code for the GUI client, server, and tests (in the form of a 
  tagged GitHub repository).  All code should be well documented with docstrings.
* A detailed `README` describing the final performance and state of your
  project.  This should include a basic instruction manual for your GUI 
  client, an API reference guide for your server, and a description of your
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

