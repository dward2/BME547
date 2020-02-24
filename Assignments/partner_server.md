# Server Assignment With Partner

In this assignment, you will work with a classmate on a shared GitHub 
repository.  You will each develop separate servers and jointly develop a 
client program that accesses and combines data from the two servers.

##  Functional Specifications

### Both Servers Should...
* Implement the following endpoints:
  * GET URL/time
    * returns the current time (time only, no date)
  * GET URL/date
    * returns the current date (date only, no time)
* Whenever a call is made to the server, a log entry is made to a file called
`server_#.log` where `#` is either `1` or `2` depending on the server.  The log entry 
should include the date and time of the call and what endpoint was called.
* The servers should run on the local host.

### Server One Should...
* Run on port 5000
* Implement the following additional endpoints:
  * POST URL/age
    * receives a JSON in the following format:  
      `{'date': "10/10/1999", 'units': "years"}`
    * returns the length in time between the current date and the date given
    in the json in years (rounded to the first decimal.  Ex: `16.2`)
  
### Server Two Should...
* Run on port 5001
* Implement the following additional endpoints:
  * POST URL/calorie_needs
    * receives a JSON in the following format:  
      `{'age': 45, 'gender': "female"}`  
      where `age` could be any number and `gender` is either `"male"` or 
      `"female"`.
    * returns a value with the estimated calorie need for a person of the 
    given age and gender.  The website <https://health.gov/our-work/food-nutrition/2015-2020-dietary-guidelines/guidelines/appendix-2/>
    can be used to determine the appropriate response.
    
### Client Program Should...
* Receive input that specifies a patient date of birth and gender.  This input 
can be obtained by entry from the console or from a text file and in whatever
format you choose.
* Calls server 1 to determine the age in years of the patient based on the 
entered date of birth.
* Calls server 2 to determine the estimated calorie need for the patient based
on their age and gender.
* Outputs this result to the screen.
* Creates a log entry in a file called `client.log` that includes the entered
date of birth, gender, calculated age, and estimated calorie result for each
patient analyzed.  This log should not be erased when the program is re-run.

## Assignment Approach
* A single GitHub repository will be used by both team members.
* One team member will be responsible for developing Server 1.
* The other team member will be responsible for developing Server 2.
* Document in `README.md` which team member is responsible for which server.
* You may collaborate on the design and development of the servers, but the 
commits must be made by the assigned team member. 
* Both team members will work together on developing the client program.  The
function that makes a request to a server should be written by the team member
who was responsible for that particular server.  Commits from both team members
should be made to this client program.
* Feature branches should be used as appropriate.

## Expectations
* A `README.md` file exists with detailed instructions on 
  * how to start the two servers
  * how to start the client program
  * how to use the client program, in terms of how inputs are made, either 
  through the console or a text file.
 
