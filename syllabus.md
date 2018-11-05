# BME 547 - Medical Software Design - Spring 2019  


## Instructors
Dr. Adam Wax  
<a.wax@duke.edu>  
Office Hours: TBD ()

Dr. David Ward  
<david.a.ward@duke.edu>  
Office Hours: TBD ()

## Teaching Assistants
FirstName LastName  
<email@duke.edu>   
Office Hours: TBD (location)

## Lecture
Wed/Fri 1:25 pm --2:40 pm  
Location TBD

## Course Overview
Software plays a critical role in almost all medical devices, spanning device
control, feedback and algorithmic processing.  This course focuses on software
design skills that are ubiquitous in the medical device industry, including
software version control, unit testing, fault tolerance, continuous integration
testing and documentation.  Experience will be gained in Python and and potentially 
other languages.

The course will be structured around various software projects related to
medical devices that measure and process a biosignal, sends it to a web
server, and makes those data accessible to a web client / mobile application.
The projects will be designed to develop software
design fundamentals.   Some project-related work will be done in groups.

## Prerequisites
Basic familiarity with programming concepts (e.g., variables, loops,
conditional statements).

BME 271 - Signals and Systems

## Course Objectives
* Software version control (`git`, GitHub)
* Device programming fundamentals
  + Review of data types, variables, loops, conditional statements
  + Python (v3.6): numpy, scipy, pandas, scikit
  + Virtual environments & dependency management (`pip`, `requirements.txt`)
  + Use of a programming IDE
  + Debugging (`pudb`)
* Testing
  + Unit testing
  + Functional / System testing
  + Continuous integration (Travis CI)
* Fault tolerance (raising exceptions)
* Logging
* Resource profiling (`cProfile`)
* Documentation
  + Docstrings
  + Markdown
  + Sphinx
  + [ReadTheDocs](https://readthedocs.org)
* Working with data
  + Data Storage (Text, Binary, HDF5, MongoDB)
  + Data Wrangling
* Data Processing & Display
  + Jupyter Notebooks
  + Matplotlib / Seaborn
  + Pandas (DataFrames)
  + [scikit-image](https://scikit-image.org/) & [scikit-learn](http://scikit-learn.org/stable/)
* Define software specifications and constraints (Requests for Comments, RFC)
* Servers
  + Design & Implementation of a biomedical web service (Python Flask)
  + HTTP & RESTful APIs
  + Docker and dependency management intro

## Attendance
Lecture attendance and participation is important because you will be working
in small groups most of the semester.  Participation in these in-class
activities will count for 15\% of your class grade.  It is very understandable
that students will have to miss class for job interviews, personal reasons,
illness, etc.  Absences will be considered **excused** if they are
communicated to your instructors at least 48 hours in advance (subject
to instructor discretion as an excused absence) or, for illness, through
submission of a [Short Term Illness Form
(STIF)](http://www.pratt.duke.edu/undergrad/policies/3531) **before** class.
Unexcused absences will count against the participation component of your class
grade.

## Textbooks & Resources
There are no required textbooks for this class.  A variety of online resources
will be referenced throughout the semester.  

* [Python Resources](Resources/python.md)

## Project Details
Project details will be discussed in lecture throughout the semester.

## Grading
Assignments will be hosted in the course GitHub repository, GitHub Classroom,
and Sakai.
Due dates--including those that change--will be announced in lecture and by
Sakai announcements that will be emailed to the
class.  

The following grading scheme is subject to change as the semester progresses:
<table>
<tr>
<td>Participation</td>
<td>15%</td>
</tr>
<tr>
<td>Assignments</td>
<td>35%</td>
</tr>
<td>Final project</td>
<td>50%</td>
</tr>
</table>

## Class Schedule
The course schedule is very likely to change depending on progress throughout
the semester.  The updated [schedule](schedule.md) will always be available in
the GitHub course repository.  

## Distributed Version Control Software (git)
Software management is a ubiquitous tool in any engineering project, and this
task becomes increasingly difficult during group development. Version control
software has many benefits and uses in software development, including
preservation of versions during the development process, the ability for
multiple contributors and reviewers on a project, the ability to tag
*Releases* of code, and the ability to branch code into different functional
branches.  We will be using [GitHub](https://github.com) to centrally host our
git repositories.  When working in teams, we will be creating student teams in the [Duke
BME Design](https://github.com/Duke-BME-Design) group.  Some guidelines
for using your git repositories:

* *All* software additions, modifications, bug-fixes, etc. need to be done in
  your repository.
* The *Issues* feature of your repository should be used as a "to do" list of
  software-related items, including feature enhancements, and bugs that are
  discovered.
* There are several repository management models that we will review in class,
  including branch-development models that need to be used throughout the
  semester.
* Instructors and teaching assistants will only review code that is committed
  to your repository (no emailed code!).
* All of the commits associated with your repository are logged with your name
  and a timestamp, and these cannot be modified.  Use descriptive commit
  messages so that your group members, instructors, and teaching assistants can
  figure out what you have done!!  You should not need to email group members
  when you have performed a commit; your commit message(s) should speak for
  themselves.
* Code milestones should be properly tagged.
* Write software testing routines early in the development process so that
  anyone in your group or an outsider reviewing your code can be convinced that
  it is working as intended.
* Modular, modular, modular.
* Document!
* Make commits small and logical; do them often!

We will review working with git repositories in lecture, and feedback on your
software repository will be provided on a regular basis.

## Online Slack Channels
We have online help through the [Duke Co-Lab
Slack](https://dukecolab.slack.com/) team. We have started three specific
channels for this class: `#linux`, `#git` & `#python`. Please add yourselves to
these channels to get help from your instructors, your TAs and the Duke
community!

## Duke Community Standard & Academic Honor
Engineering is inherently a collaborative field, and in this class, you are
encouraged to work collaboratively on your projects.  The work that you submit
must be the product of your and your group's effort and understanding.  All
resources developed by another person or company, and used in your project,
must be properly recognized.

All students are expected to adhere to all principles of the [Duke Community
Standard](http://www.integrity.duke.edu/standard.html).  Violations of the Duke
Community Standard will be referred immediately to the Office of Student
Conduct.  Please do not hesitate to talk with your instructors about any
situations involving academic honor, especially if it is ambiguous what should
be done.
