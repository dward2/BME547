# Web Services, APIs, and Requests
## Introduction
Modern software design almost always has some relationship to cloud computing.
The ability for local software and applications to access the cloud allows
for improved information sharing, access to enhanced computing power, and 
increased data storage and access.

For example, in designing a medical device, we may want it to be portable,
affordable, and have a long battery life.  These criteria may make it difficult
to design a device with the computing power desired.  If the device can
access a more powerful device or server in the cloud, it can offload the 
heavy-duty computation and data storage needed for its functioning and still
be able to be lightweight (in both size and performance).

Therefore, we need to learn how to make interact with web services with our
software and how to design those web services.

## APIs
An Application Programming Interface (API) provides instructions or an 
interface for accessing the functionality of a program or package.  

Let's think of a physical example.  Assume you have a toaster.  How does the
toaster actually work?  It takes electricity, sends it through a resistive
heating element at a certain voltage for a certain time.  A timer eventually
turns off the heat, generates some sort of signal, and maybe even eject the 
toast.  When you use a toaster, you don't specifically set current levels or
turn on the element, or monitor temperatures.  You simply press some buttons.
The buttons you press (on/off, toast darkness, timer) could be thought of
as the API that allows the user to access the functionality of the toaster.

Let's think about the packages you have used so far in this class.  Take
the `scipy` package.  There is lots of code in it to do all kinds of
calculations:  for example, the peak finding routines you may have used
for the ECG Analysis assignment (`scipy.signal.find_peaks`).  This function
call allows you to access some of the calculation methods within `scipy`.  The
`find_peaks` function is part of the API for `scipy`.  

For programming, APIs can be thought of as the functions of a package or
program that users can use.  In the `scipy` example, a user can go to the 
API Reference (<https://docs.scipy.org/doc/scipy/reference/#api-reference>) for
`scipy` and find all of the functions that can be used.  `find_peaks` can
be found at <https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html#scipy.signal.find_peaks>

APIs are also useful to provide a consistent interface to a program's 
functionality that won't change over time as the program grows/updates/changes
or is implemented on different platforms (PC/macOS/Android).

Your challenge as a developer:  to design an API for your software/services
that is user-friendly and will be stable over a period of years.