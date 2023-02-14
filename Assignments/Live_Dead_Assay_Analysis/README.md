# Live/Dead Cell Assay Analysis Assignment

## Background

In pharmaceutical drug studies, it is important to know the impact of 
potential drugs on the health of cells.  A Live/Dead cell assay is a method
of identifying live cells from dead or dying cells after exposure to a 
particular drug or condition.  Two fluorescent dyes are added to the cell
mixture.  CalceinAM will stain live cells and will fluoresce green.  EthD-III
will stain dead or dying cells and will fluorsce red.  An image of the 
fluorescing cells is then taken.  Computer analysis of the image can count
the number of green and red cells to determine the relative ratio of live vs.
dead cells.  

For this assignment, we will be writing some code that reads in patient data
containing simplified image information, analyzes the images, and then creates
separate output files for each patient.

## Input Data
A sample input file is found in a text file called `sample_data.txt` in this
repository.  

The data for a single patient is formatted as follows:
```
FirstName Lastname
DOB
GREEN
#,#,#,#,...,#
#,#,#,#,...,#
#,#,#,#,...,#
#,#,#,#,...,#
...
#,#,#,#,..,,#
RED
#,#,#,#,...,#
#,#,#,#,...,#
#,#,#,#,...,#
#,#,#,#,...,#
...
#,#,#,#,..,,#
```

The first line will have the first and last name of the patient separated by a
space.  
Example:  `Anne Boynton`

The second line will have the date of birth of the patient, formatted as 
`mm/dd/yyyy`.  
Examples:  `09/02/1974`; `12/23/2001`

The third line will have the string `GREEN` to indicate that the image data
on the following lines will be for the "Green" channel of the RGB image.  

The image data follows and is split up into rows and columns, with an equal
number of rows and columns.  So, the image is square.  Each row will 
contain integers between 0 and 255, separated by commas.  The number of data 
points on each row will equal the number of rows that exist for the image.

Example (for Green channel):
```
3,10,3,98,9
13,15,16,2,9
174,11,253,4,7
2,12,5,10,0
1,8,9,5,104
```
Note, there are five data points on each line and there are five row, meaning
the image is 5x5.

After the "Green" image data is shown, the next line will have the string `RED`
to indicate that the image data on the following lines will be for the "Red"
channel of the RGB image.  This data will be exactly the same size as the 
"Green" data in terms of the number of points per line and the number of lines.

Example (for Red channel):
```
2,75,158,8,235
232,7,11,11,9
5,8,7,2,9
13,240,10,238,16
236,181,2,7,1
```

The input file will contain multiple patients sequentially with no blank lines
or other indicators between them.  So, immediately after the last data line of
"Red" data for a patient, the next line will contain the name of
the next patient.

After the last patient, the file will have a line containing `END` to mark the
end of the file.

Note that the image size for each patient may vary.  So, while one patient may
have a 5x5 image, another may have a 7x7 image while another may be 12x12.

Your assignment will be graded on a different input file than the sample
provided.  However, the format as described above will be the same.  Your code
does not need to account for "mistakes" in the format.  The file will be 
formatted correctly.  But, your code must be able to handle files with any
number of patients and with different image sizes.

## Image Analysis
The image is a square grid with each grid point being measured for the 
color that fluoresces there.  This color is analyzed as an RGB value.  RGB 
stands for **R**ed, **G**reen, **B**lue, the three channels of which, when
combined, yield a color.  Each channel is quantified as a value between 0 and 255.

To analyze the image, look at the green and red values for each data point.  If
the green value is **greater than or equal to 75**, then that data point
represents a "live" cell.  If the red value is **greater than or equal to 75**,
the that data point represents a "dead" cell.  If neither value is greater than
75, there is not a cell at that data point.  It is not possible for both the
green and red data to be greater than 75.

Using the example above for the "Green" channel, there are four values of 75
or greater, so there are 4 live cells in the image.  For the "Red" channel,
there are 8 values of 75 or greater, so there are 8 dead cells.  That leads
to a total cell count of 12.  The live fraction is 4 / 12 = 0.33.  The dead
fraction is 0.66.  The cell density fraction is the number of total cells (12) 
divided by the total number of image data points (5x5=25) for a value 
of 12 / 25 = 0.48.  

## Program Specifications
* Read input data from a text file.  `sample_data.txt` is provided as a sample,
  but the file on which your code will be graded will have different data and
  a different number of patients.  So, your code must be flexible enough to 
  handle files with different number of patients.  You may "hard-code" the 
  string `sample_data.txt` in your code for the input file name.  You do not 
  need to program any kind of file input interface.
* For each patient, determine the following:
  + Determine the total number of data points for the image (for example, if
    the image is 5x5, the total number of data points is 25).
  + Determine the number of live cells and the live cell fraction based on 
    the criteria above.
  + Determine the number of dead cells and the dead cell fraction based on 
    the criteria above.
  + Determine the cell density fraction as defined by the total number of cells
    (live + dead) divided by the total number of data points.
  + Determine the analytical result of the image based on this table:

    |   | Cell Density Fraction >= 0.4 | Cell Density Fraction < 0.4 |
    |------------|-------------------------| --- |
    | __Live Cell Fraction >= 0.7__ | PASSED     | TENTATIVE_PASS          |
    | __Live Cell Fraction < 0.7__ | FAILED   | TENTATIVE_FAIL          |

* For each patient, create an individual output file with the name 
  "FirstName-LastName.json" where FirstName and LastName are replaced with the
  first name and last name of each patient.  Example:  `Anne-Boynton.json`.
* This output file should contain a dictionary in JSON format with the
  following keys and corresponding values:
  + `First Name`, value is a string containing the patient's first name.
  + `Last Name`, value is a string containing the patient's last name.
  + `DOB`, value is a string containing the patient's data of birth formatted
    as `mm/dd/yyyy` (same as in input file).
  + `Cell Total`, value is an integer that is the total number of cells (live
    and dead) detected in the image.
  + `Live`, value as a float that contains the fraction of cells which are
    live.  This should be a value between 0 and 1.0 and rounded to a maximum of
    two decimal places.
  + `Dead`, value as a float that contains the fraction of cells which are
    dead.  This should be a value between 0 and 1.0 and rounded to a maximum of
    two decimal places.
  + `Result`, value is a string containing one of the results as determined
    by the table above.  The results string should be exactly as shown in the
    table.
* To create the above JSON output file, first create a dictionary with the keys
  listed exactly as above and assign each key the corresponding value.  Then,
  using the `open` and `json` commands, create the file and output the 
  information.

### Notes
* In the dictionary/JSON description above, when a value is indicated to be a
  float or integer, it should NOT be a string containing a float or integer,
  but an actual number.
* Remember that when a line of text is read in by Python, it may have a return
  character, `\n`, at the end which you will need to account for.


## Grading Expectations
* Good git usage and workflow
* Meeting the above functional specifications
* Appropriate functional modularity that will allow for appropriate unit tests
* Unit testing exists for all functions that do any algorithmic work, excluding
  input/output routines
* Conforms to PEP-8 Style Guide 
* GitHub Actions CI integration with all branches passing unit tests and PEP-8 
  style before merge
* Docstrings exist for all functions
* Appropriate use of virtual environments as demonstrated by a
  `requirements.txt` file being present in your GitHub repository
* Presence and content of README.md (at a minimum including author information,
  a description of the purpose of the repository, and how to execute your
  program)
* Final submission is pushed to GitHub by the deadline and is tagged 
  appropriately
* Plus any expectations from previous assignments
