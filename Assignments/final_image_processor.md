# Image Processor Final Project (Fall 2019)

**Final Project DUE:** Wednesday, December 11, 2019, 9:00 AM EST 

## Overview
The final project in this class will require your team to leverage the
industry-standard skills you've learned over this semester to design and
implement a software system to upload an image or an archive of images to a
web-server, perform image-processing tasks on the web-server, and then display
/ download your processed image(s).  You will be required to work in 
groups for this projects.

This final project is somewhat open-ended to allow groups to tailor this to
their areas of interest; however, recommended datasets and project requirements
are provided below.  If you plan to stray away from the recommended projects
and datasets, please submit a one-page project proposal to Dr. Ward
by *Friday, November 22, 2019* for evaluation to ensure the proposed
project meets the requirements for the class. Be sure to include motivations,
technologies, functional specifications, and anticipated deliverables.

It is expected that your team will follow proper professional software
development and design conventions taught in this class, including:
* git feature-branch workflow
* continuous integration
* unit testing
* PEP8
* docstrings / Sphinx documentation

**You should approach this final project as an opportunity to show a potential
future employer an example of your software development skills.**

## Functional Specifications
### GUI Client
At a minimum, you image processor client should do the following:
* Provide a __graphical__ user interface that will allow a user to select an image, list of
  images, or a zip archive of images for upload to your web-server,
  and then issue a RESTful API request
  to your cloud service to upload the images and do any further processing.
  
* In addition to uploading the raw image, your __graphical__ user interface 
should give the user a choice of processing steps that the server should
perform on the uploaded image, including:
  + Histogram Equalization __default__
  + Contrast Stretching
  + Log Compression
  + Invert Image  
  (colors, not orientation  example: ![](support_files/pup.jpg) to ![](support_files/invert_pup.jpg))  
  The processed image should also be stored on the server.

* Your user interface should also provide:
  + The ability to choose, display, and compare original and processed images 
  from the server.
  + An option to download the image(s) from the server in one of the following 
  formats:
    - JPEG
    - PNG
    - TIFF  
  If multiple images are to be downloaded, they should be downloaded as a zip archive.
  + Display histograms of the image color / intensity values of the original and processed images.
  + Display useful metadata of displayed images, including:
    - Timestamp when uploaded
    - CPU time required to process the image(s)
    - Image size (e.g., X x Y pixels)
  + Ability to retrieve from the server and display the user actions/metrics 
  tracked by the server as described below. 
  
### Cloud Server
At a minimum, your image processor server should do the following:
* Be a cloud-based web service running on your virtual machine that exposes 
a well-crafted RESTful API that will
  implement the image processing methods specified above (check out
  [scikit-image](http://scikit-image.org/) to make your life easier on the image processing algorithms!).
  

* Allow for multiple, unique users to upload and retrieve their files.

* A persistent database should be implemented in some form to do the following:  
  + Store user actions / metrics, including how many image uploads the user has
  made and the total number of times the user has called each of the various 
  image processing steps. 
  + Store uploaded images and timestamps for a user
  + Store processed images (along with what processing was applied) and timestamps for a user

**Note**: The GUI should only make requests to the server and should not make 
contact with the database.  All database functions should be handled from the
server.  If the GUI needs to interact with the database, it should do it by
making requests of the server. 

## Deliverables
* A detailed `README` describing the final performance and state of your
  project.  This should include a basic instruction manual for your GUI client.
* Recorded video demo of your image processor in action.
* All project code for GUI client, server, and tests (in the form of a tagged 
GitHub repository)
* Link to deployed web service in your`README.md`.
* Sphinx-generated documentation pushed to GitHub repository.  This should
include information about your server API.

## Recommended Datasets
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