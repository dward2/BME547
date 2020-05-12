# BME 547 - Medical Software Design - Summer 2020  

## Instructor
Dr. David Ward  
<david.a.ward@duke.edu>  
Office Hours: By appointment

## Teaching Assistant

## Remote Learning Delivery 
This course is being offered via remote learning.  A computer and good internet
connection are required.  Live, interactive class periods will be held via
Zoom on **Mon/Tues/Wed/Thur 10:00 am -- 11:30 AM**.  It is expected that
students will participate in these meetings whenever possible.  These class
meetings will be recorded for those who are unable to attend (due to timezone 
or technological issues) for viewing at a different time.

Some lecture content may be delivered via pre-recorded videos that should be
watched before class.  There will also be some "daily assignments" that will
be conducted either during class or will be expected to be completed before
class in preparation for a class period.  Again, for those who cannot attend 
class, these daily assignments can be done at a different time, but will be
expected to be completed within 24 hours of the assigned class period.  

Sakai will be used for official course communication.  Zoom Meeting Links 
will be posted in Sakai.

About nine projects will be assigned throughout the semester.  The description
of these assignments will be posted in Sakai and also in this GitHub repo.
Assignments will be turned in via a GitHub Classroom repository.

## Course Overview
Software plays a critical role in almost all medical devices, spanning device
control, feedback and algorithmic processing.  This course focuses on software
design skills that are ubiquitous in the medical device industry, including
software version control, unit testing, fault tolerance, continuous integration
testing and documentation.  Experience will be gained in the Python programming
language.

The course will be structured around various software projects related to
medical devices and databases that measure and process biosignals, send 
information to a web server, and makes those data accessible to a web client.
The projects will be designed to develop software
design fundamentals.   Some project-related work will be done in groups.

## Prerequisites
Basic familiarity with programming concepts (e.g., variables, loops,
conditional statements, functions and parameters).

BME 271 - Signals and Systems

A computer with administrator rights and good internet connection.

## Course Topics
* Software version control (`git`, GitHub)
* Device programming fundamentals
  + Review of data types, variables, loops, conditional statements
  + Python (v3)
  + Use of external libraries / packages
  + Virtual environments & dependency management (`pip`, `requirements.txt`)
  + Use of a programming IDE
  + Debugging (`pudb`)
* Testing
  + Unit testing
  + Functional / System testing
  + Continuous integration (Travis CI)
* Fault tolerance (handling and raising exceptions)
* Logging
* Documentation
  + Docstrings
  + Markdown
  + Sphinx
  + [ReadTheDocs](https://readthedocs.org)
* Working with data
  + Data Storage (Text, Binary, MongoDB)
* Data Processing & Display
  + Jupyter Notebooks
  + Matplotlib
  + Pandas (DataFrames)
  + [scikit-image](https://scikit-image.org/) & [scikit-learn](http://scikit-learn.org/stable/)
* Servers
  + Design & Implementation of a biomedical web service (Python Flask)
  + HTTP & RESTful APIs
* Define software specifications and constraints (Requests for Comments, RFC)

## Attendance / Participation
Lecture attendance and participation is important as the topics and skills you
will be learning build upon each other.  Also, you will be working
in small groups some of the semester.  Various "daily assignments" will also 
be given as part of either class period preparation or during the class 
period itself.  

As stated above, it is understood that some class members may not be able to 
join the class periods due to timezone or technology reasons.  In those cases,
it is expected that those students will view the Zoom meeting recordings and
complete the given daily assignment within 24 hours of assignment.  

Completion of these assigned in-class activities (either during class or later)
will count for 15\% of your class grade.  It is very understandable
that students will have to miss class for job interviews, personal reasons,
illness, etc.  Absences or delayed daily work will be considered **excused** 
if they are
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
<table>
<tr>
<th>Grading Breakdown</th><th></th>
</tr>
<tr>
<td>Participation / In-Class Assignments</td>
<td>15%</td>
</tr>
<tr>
<td>Assignments</td>
<td>45%</td>
</tr>
<tr>
<td>Final project</td>
<td>40%</td>
</tr>
</table>

All work is due by the date and time posted in Sakai.  No late submissions will
be accepted without prior approval for an excused reason.  You will
be given the opportunity to submit *one* assignment up to 48 hours late 
for any reason without penalty if you notify me that you are utilizing that
option before the deadline via e-mail.    

## Class Schedule
The course schedule is very likely to change depending on progress throughout
the semester.  The updated [schedule](schedule.md) will always be available in
the GitHub course repository.  Assume there will be lecture every class period
even if no topic is shown on the schedule.

## Distributed Version Control Software (git)
Software management is a ubiquitous tool in any engineering project, and this
task becomes increasingly difficult during group development. Version control
software has many benefits and uses in software development, including
preservation of versions during the development process, the ability for
multiple contributors and reviewers on a project, the ability to tag
*Releases* of code, and the ability to branch code into different functional
branches.  We will be using [GitHub](https://github.com) to centrally host our
git repositories.  Some guidelines for using your git repositories:

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

## Duke Community Standard & Academic Honor
Engineering is inherently a collaborative field, and in this class, you are
encouraged to discuss what you have learned in class and share resources that
you find.  However, your code development and final submitted code must be the 
product of your and/or your group's effort and understanding.  It is not 
permitted to share your code with others for them to copy or use.  Any external 
resources developed by another person or company, and used in your project,
must be properly recognized.

All students are expected to adhere to all principles of the [Duke Community
Standard](http://www.integrity.duke.edu/standard.html).  Violations of the Duke
Community Standard will be referred immediately to the Office of Student
Conduct.  Please do not hesitate to talk with your instructors about any
situations involving academic honor, especially if it is ambiguous what should
be done.
