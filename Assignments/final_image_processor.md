# Patient Monitoring Client/Server Project

## Overview
The final project in this class will require you to leverage the
industry-standard skills you've learned during this semester to design a 
Patient Monitoring
System that has a patient-side client, a monitoring-station client, and a
server/database that allows patient data to be uploaded and stored on the
server and retrieved for ad-hoc and continuous monitoring.

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
At a minimum, your patient-side GUI client should provide a __graphical__ user 
interface with the following functionality:
  + Allow the user to enter a patient name.
  + Allow the user to enter a patient medical record number.
  + Allow the user to select and display a medical image from the local 
  computer.
  + Allow the user to select an ECG data file from the local computer.  This
  ECG data should then be analyzed for heart rate in beats per minute, display 
  the resulting heart rate in the GUI, and display an image of the ECG 
  trace in the interface.
  + Upon user command, issue a RESTful API request to your server to upload
  whatever information is entered above.  The interface should only allow this
  request to be made if at least a medical record number has been entered.
  Data to upload should include the medical record number and the following,
  if uploaded:  patient name,
  measured heart rate & ECG image, and medical image.  If an item was not
  selected or added, it does not need to be uploaded.  
  + After upload, the information entered in the GUI should REMAIN in the GUI 
  so it can still be seen.  
  + The user should have the ability to update any of this information in the
  GUI and upload the new information to the server.  If the patient name is
  updated in the GUI, it should be replaced in the server.  If a new heart
  rate/ECG image or medical image is updated in the GUI, this new information
  should be added to the existing information on the server.
  + The user should have the ability to delete/clear this information from the
  GUI so that a new patient can be entered without having to exit the GUI.  

For the ECG analysis of heart rates, please use your existing ECG analysis 
code module, and modify it with a function that your GUI can call to execute
your code to do the 
analysis.  The ECG data files will be the same test files from the ECG Analysis
assignment.  This ECG code will not be re-evaluated and does not need unit
tests (although it will still need to pass PEP-8 testing).  The only evaluation
that will be made is that you call this function correctly from the GUI code
and receive the heart rate back correctly.  You don't need the correct heart
rate (i.e., whatever heart rate your code measured for the original ECG 
assignment will be considered the correct heart rate for this assignment).  
   
### Monitoring Station GUI Client
At a minimum, your monitoring-station GUI client should provide a __graphical__
user interface with the following functionality:
  + Allow the user to select a patient medical record number from a list of 
  available numbers on the server.
  + For the selected patient, display the medical record number, the patient
  name, the latest measured heart rate & ECG image (if one exists), and 
  the date/time at which this latest heart rate data was uploaded to the server.
  + Allow the user to select from a list of historical ECG images and their 
   date/times for the selected patient, download the selected image, and 
   display the selected image side-by-side with the latest ECG image already 
   displayed.
  + Allow the user to save a downloaded ECG image (either the latest or the
    historical one chosen) to a file on their local computer.
  + Allow the user to select from a list of saved medical images for this 
  patient, download and display the image, and allow it to be saved locally.
  + When the user selects a new patient, any information from the previous
  patient on the interface needs to be replaced with the information from the
  new patient or removed from the interface.
  + The interface should make periodic requests (at least every 30 seconds, but
  can be more frequent) to the server to check for any updated information for
  the currently selected patient.  If a new heart rate and ECG image are 
  available, those should be automatically downloaded and displayed on the 
  interface.
  + When the user wants to select a new patient, select an historical ECG, or
    select a medical image for a patient, the choices should represent the 
    most recent options on the server.  In other words, the options for choices
    must dynamically update, rather than be "locked in" based on what was 
    available when the client was started.  
  + In order to complete these tasks, the client GUI will need to make RESTful 
  API requests to the server to get lists of available patient medical record
  numbers, available data for the selected patient, and the data/images 
  themselves.

### Cloud Server
At a minimum, your server should be a cloud-based web service running on your 
virtual machine that exposes a well-crafted RESTful API that will implement 
the tasks needed by the clients as described above and outlined here:

* Accept uploads from the patient-side client that will include, at a minimum,
the medical record number.  The upload may also include a name, medical image, 
and/or heart rate & ECG image.
* Communicate with and utilize a persistent database that will store the above
uploaded data for retrieval at a future time.  
* When a heart rate and ECG image are received, the date and time of receipt 
should be stored with the data.
* If the upload contains a medical record number not already found in the 
database, a new entry should be made for that patient, and the information 
  sent with the request stored in this new record.  
* If the upload contains a medical record number already found in the database,
any medical image and/or heart rate/ECG image sent with the request should be
added to the existing information. If a patient name is also sent, it should 
update the existing name in the database.
* Accept requests from the monitoring station client to retrieve the following
information from the database and download it to the client:
  + a list of available patient medical record numbers
  + the name and latest heart rate & ECG image for a specific patient
  + a list of ECG Image timestamps for a specific patient
  + a list of medical images for a specific patient
  + a specific ECG Image based on timestamp for a specific patient
  + a specific medical image for a specific patient  
  __Note__: The above list does not imply that you must have one route for
  each of those items.  Just make sure your server provides the needed 
  services.
* Provide any other services as needed for the client to perform its needed
functions.

**Note**: The GUIs should only make requests to the server and should not make 
contact with the database.  All database functions should be handled from the
server.  If the GUI needs to interact with the database, it should do it by
making requests of the server. 

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

**Medical Images**

Your GUI should allow the user to choose any image they like on their computer,
which may or may not be found in the repository folder,
not just the sample images provided in the starting repository.  Those are
provided simply as examples of the types of images I will be using when testing
your program.  Feel free to use these for your testing.  Also, I will not be
trying to upload any unusual image formats.  So, you do not need to program
the GUI to handle obscure formats.  As long as it works for standard formats,
(e.g., JPG), it will be fine.
