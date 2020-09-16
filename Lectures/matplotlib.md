# Matplotlib
Matplotlib is a Python 2D plotting library to make customizable, high-quality
figures in a variety of formats.  The `pyplot` module of Matplotlib provides
a MATLAB-like interface.  

## Importing Matplotlib
The `matplotlib` package must be installed in your virtual environment.

Then, the `pyplot` module can be imported as follows:
```
import matplotlib.pyplot as plt
```
## Basic Plot Commands
Here is some code to make a simply x-y scatter plot.
```
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]
plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("My First Plot")
plt.show()
```
![myplot.png](matplotlib_files/myplot.png)

We can control how the data is plotted by adding a third argument to the 
`.plot()` function.  When this third argument is not given, the default of 
`"b-"` is used which is a blue line as shown in the plot above.  If the code
is changed as shown below to include a third argument of `"ro"`, it plots
red dots (see below).  Also, the `.axis()` sets the scale of
the x and y axes.
```
plt.plot(x, y, "ro")
plt.axis([-1, 10, -5, 45])
```

![myplot2.png](matplotlib_files/myplot2.png)  

To add a second data series to the plot, add these lines to the code:
```
z = [35, 30, 25, 30, 25, 20]
plt.plot(x, z, "g-")
```
![myplot3.png](matplotlib_files/myplot3.png)

## References
* General Matplotlib website:  https://matplotlib.org/
* Intro to using `pyplot` module:  https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

<!--- Removed because using Jupyter Notebooks for intro, which asks to do
this exercise.
## In Class Exercise
* Write a function that generates two `numpy` arrays:
  - `time` that contains linear values from 0 to 10
  - `y` that contains the `sin` of the values in `time`
  -  Use the function `np.sin()`
* Generate a plot of `y` vs. `time` using `matplotlib`
--->

## Troubleshooting
If you are using linux (or sometimes macOS), when trying to run Matplotlib,
you may get an error that says something like `Your currently selected backend, 
'agg' does not support show().`  If you get this error, or something of the
like, it may be that you do not have the `tkinter` package installed.  If that
is the case, you will need to install it as follows:
```bash
sudo apt-get install python3-tk
```
