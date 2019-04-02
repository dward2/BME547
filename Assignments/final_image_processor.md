# Image Processor Final Project (Spring 2019)

**Final Project DUE:** Friday, April 26, 2019 11:59 PM EST 

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
and datasets, please submit a one-page project proposal to Dr. Palmeri and Mr.
Kumar by *Friday, April, 13, 2018* for evaluation to ensure the proposed
project meets the requirements for the class. Be sure to include motivations,
technologies, functional specifications, and anticipated deliverables.

It is expected that your team will follow proper professional software
development and design conventions taught in this class, including:
* git feature-branch workflow
* continuous integration
* unit testing
* PEP8
* docstrings / Sphinx documentation

## Functional Specifications
At a minimum, you image processor should do the following:
* Provide a [graphical] user interface that will allow a user to select an image, list of
  images, or a zip archive of images that will be uploaded to your web-server,
  perform necessary preprocessing steps, and then issue a RESTful API request
  to your cloud service for further processing.
* Your [graphical] user interface will have a choice of processing steps to perform on each
  uploaded image, including:
  + Histogram Equalization [default]
  + Contrast Stretching
  + Log Compression
  + Reverse Video
  + Others of your choice!
* A cloud-based web service that exposes a well-crafted RESTful API that will
  implement the image processing methods specified above (checkout out
  [scikit-image](http://scikit-image.org/) to make your life easier on the image processing algorithms!).
* A database should be implemented in some form to do one or more of the following:
  + Store previous user actions / metrics (e.g. how many times has a user run Histogram Equalization, 
  latency for running different processing tasks, etc). 
  + Store uploaded images and timestamps for a user
  + Store processed images (along with what processing was applied) and timestamps for a user
  + Another use case you choose.
* Your user interface should also provide:
  + An option to display and compare the original and processed images.
  + An option to download the image(s) in one of the following formats:
    - JPEG
    - PNG
    - TIFF
  If multiple images are to be downloaded, they should be downloaded as a zip archive.
  + Display histograms of the image color / intensity values of the original and processed images.
  + Display useful metadata, including:
    - Timestamp when uploaded
    - Time to process the image(s)
    - Image size (e.g., X x Y pixels)

## Deliverables
* A detailed `README` describing the final performance and state of your
  project.
* Recorded video demo of your image processor in action.
* All project code (in the form of a tagged GitHub repository named
  `bme590final`)
* Link to deployed web service 

## Recommended Datasets
Your project can utilize some existing databases of image (or you can choose to
use your own images).  Here are some example datasets that you can access for
this project:

* Over 13000 annotated skin lesion images are available from the International
  Skin Imaging Collaboration (ISIC) project that can be used to develop machine
  learning models to classify new images. This dataset can be accessed here:
  https://isic-archive.com. A zip of all annotated images can be downloaded by
  navigating to the Gallery and then clicking "Download as Zip" in the upper
  right hand corner. All data can also be accessed through a RESTful API
  provided by the ISIC.
* http://www.vision.caltech.edu/Image_Datasets/Caltech101/
* https://www.cs.toronto.edu/~kriz/cifar.html
* https://github.com/beamandrew/medical-data

## Grading
**You should approach this final project as an opportunity to show a potential
future employer an example of your software development skills.**

* Git Repository
  + Issues/Milestones
  + Commits are discrete, logical changesets
  + Feature-branch workflow
* Software best practices
  + Modularity of software code
  + Handling and raising exceptions
  + Language convention and style (PEP8)
  + Sphinx documentation for all modules/functions
* Testing and CI
  + Unit test coverage of all functions (except Flask handler)
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