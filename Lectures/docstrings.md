# Docstrings

Docstrings are used to annotate functions to provide:
* One-line summary of function
* More verbose description of function
* Input parameters
* What is returned

Relevant Python documentation: https://www.python.org/dev/peps/pep-0257/

There are three common docstring styles that can be used:
* [reStructuredText Docstring Format](https://www.python.org/dev/peps/pep-0287/)
* [Numpy Style Python Docstrings](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
* [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
  (also https://google.github.io/styleguide/pyguide.html)

`reStructuredText` docstrings are the "default" for most IDEs and code editors,
but it can be difficult to read (IMO).  Numpy and Google-style docstring tend
to be more readable in "raw" form, and can be easily compiled into full
documentation using the
[Napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html#)
[Sphinx](sphinx.md) extension.

## Links
Example of finished documentation:
https://mlp6.github.io/fem/

Code for this example: https://github.com/mlp6/fem

## Style Examples
### reStructured Text
```
def BMI_calculation(height, weight):
    """Calculate Body Mass Index from given height and weight
    
    Body Mass Index (BMI) attempts to quantify the amount of tissue mass in
    an individual and then categorize that person as underweight, normal,
    overweight or obese.  The formula for BMI is
    BMI = (mass in kg) / (height in m)^2
    https://en.wikipedia.org/wiki/Body_mass_index

    :param height: float containing the height in meters
    :param weight: float containing the weight in kilograms

    :returns: float containing the calculated BMI
    """
```

### Google Style
```
def BMI_calculation(height, weight):
    """Calculate Body Mass Index from given height and weight
    
    Body Mass Index (BMI) attempts to quantify the amount of tissue mass in
    an individual and then categorize that person as underweight, normal,
    overweight or obese.  The formula for BMI is
    BMI = (mass in kg) / (height in m)^2
    https://en.wikipedia.org/wiki/Body_mass_index

    Args:
        height (float): height in meters
        weight (float): weight in kilograms

    Returns:
        float: the calculated BMI
    """
```

### Numpy Style
```
def BMI_calculation(height, weight):
    """Calculate Body Mass Index from given height and weight
    
    Body Mass Index (BMI) attempts to quantify the amount of tissue mass in
    an individual and then categorize that person as underweight, normal,
    overweight or obese.  The formula for BMI is
    BMI = (mass in kg) / (height in m)^2
    https://en.wikipedia.org/wiki/Body_mass_index

    Parameters
    ----------
    height : float
        Contains the height in meters
    weight : float 
        Contains the weight in kilograms

    Returns
    -------
    float 
        The calculated BMI
    """
```
