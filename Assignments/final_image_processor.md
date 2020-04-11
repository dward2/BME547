# Medical Image Database Final Project (Spring 2020)

**Final Project DUE:** Monday, April 27, 2020, 9:00 AM EST 

## Overview
The final project in this class will require you to leverage the
industry-standard skills you've learned over this semester to design and
implement a software system to upload a medical image to a
web-server, store the image in a database, perform image-processing tasks on 
the web-server, and then display
/ download the original and/or processed image.  

This final project can be somewhat open-ended if you would like to tailor this to
your areas of interest.  If you plan to stray away from the recommended project
and requirements below, please submit a one-page project proposal to Dr. Ward
by *Friday, April 17, 2020* for evaluation to ensure the proposed
project meets the requirements for the class. Be sure to include motivations,
technologies, functional specifications, and anticipated deliverables.

It is expected that you will follow proper professional software
development and design conventions taught in this class, including:
* git feature-branch workflow
* continuous integration
* unit testing
* PEP8
* docstrings
* Use of issues and milestones to track development progress (new to this 
assignment)

**You should approach this final project as an opportunity to show a potential
future employer an example of your software development skills.**

## Functional Specifications
### GUI Client
At a minimum, you GUI client should do the following:
* Provide a __graphical__ user interface that will allow a user to select an 
  image for upload to your web-server, and then issue a RESTful API request
  to your cloud service to upload the image.
  
* In addition to uploading the raw image, your __graphical__ user interface 
should give the user a choice of processing steps that the server should
perform on the uploaded image, including:
<!--  + Histogram Equalization __default__
  + Contrast Stretching
  + Log Compression
  + Invert Image  
  (colors, not orientation  example: ![](support_files/pup.jpg) to ![](support_files/invert_pup.jpg))  
-->  
  The processed image should also be stored on the server.

* Your user interface should also provide:
  + The ability to choose, display, and compare original and processed images 
  from the server.
  + An option to download original or processed image(s) from the server.
  + Display useful metadata of displayed images, including:
    - Timestamp when uploaded
    - Image size (e.g., X x Y pixels)
  
### Cloud Server
At a minimum, your image processor server should do the following:
* Be a cloud-based web service running on your virtual machine that exposes 
a well-crafted RESTful API that will
  implement the image processing methods specified above (check out
  [scikit-image](http://scikit-image.org/) to make your life easier on the image processing algorithms!).
  

* A persistent database should be implemented in some form to do the following:   
  + Store uploaded images and timestamps
  + Store processed images and timestamps
  
* Provide what other services are needed for the client to perform its needed
functions.

**Note**: The GUI should only make requests to the server and should not make 
contact with the database.  All database functions should be handled from the
server.  If the GUI needs to interact with the database, it should do it by
making requests of the server. 

## Deliverables
* A detailed `README` describing the final performance and state of your
  project.  This should include a basic instruction manual for your GUI client.
* Recorded video demo of your client program in action.
* All project code for GUI client, server, and tests (in the form of a tagged 
GitHub repository)
* Link to deployed web service in your`README.md`.
* Sphinx-generated documentation pushed to GitHub repository.  This should
include information about your server API.

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

The following is a partial list of aspects of the project that will be graded.

* Git Repository
  + Issues/Milestones (New for this assignment)
  + Commits are discrete, logical changesets
  + Feature-branch workflow
* Software best practices
  + Modularity of software code
  + Handling and raising exceptions
  + Language convention and style (PEP8)
  + Sphinx documentation for all modules/functions
* Testing and CI
  + Unit test coverage of all functions (except Flask handler and GUI calls)
  + Travis CI passing build
* Cloud-based Web Service
  + RESTful API Design 
  + Validation Logic 
  + Returning proper error codes
  + Robust deployment on virtual machine 
  + Image processing functionality
* Proper use of a database 
* User interface functionality
* Demo of the final working project
* Robust README