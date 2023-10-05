# Unit Testing of Class Methods

Just as regular Python functions need to be tested, the methods written for
a class also need to be tested.  However, where a standard function has
defined inputs and outputs for testing, some class methods use internal
class properties as inputs and outputs.  This requires some additional code
in the unit test function to set up the class instance and get class
properties to assert for correct results.

## Example Class
Let's examine the following class for how we would write unit tests for its
methods.

```python
from PIL import Image


class AssayImage:

    def __init__(self, filename):
        self.image_obj = Image.open(filename)
        self.image_width = self.image_obj.size[0]
        self.image_height = self.image_obj.size[1]
        self.pixel_count = self.image_height * self.image_width
        self.anomaly_count = -1
        self.threshold = -1

    def analyze_image(self, new_threshold):
        self.threshold = new_threshold
        self.anomaly_count = self.code_to_detect_anomalies_from_image()
    
    def get_results(self):
        if self.anomaly_count < 0:
            raise RuntimeWarning("Image analysis not yet performed.  "
                                 "Call the analyze_image method first.")
        if self.anomaly_count > self.pixel_count * 0.25:
            result = "Anomalous"
        else:
            result = "Acceptable"
        return result
```

The `AssayImage` class is designed to hold an image and do an analysis on that
image based on a provided threshold value and return whether the image
represents an anomalous image or an acceptable image.

All three of the methods shown, including the `__init__` method do calculations
that need to be tested.  We need to modify our typical unit test format 
somewhat in that two of the functions do not have a specific `return` to test
and one function doesn't take any parameter inputs to send a test case.

## Unit test function naming convention for classes
The standard naming convention for our unit tests is `test_<name of function 
to be tested>`.  We will simply extend this to also include the name of the
class:  `test_<class name>_<name of method to be tested>`.  So, for example,
to test the `get_results` method of the `AssayImage` class above, the unit test
function name would be `test_AssayImage_get_results`.

## Testing of class `__init__` function
An `__init__` function of a class will need to be tested if the `__init__`
function does any of its own calculations.  If an `__init__` function only 
stores the received parameters in class properties, it does not need a unit 
test.  

The `AssayImage` class above does do some calculations in its `__init__`
function.  A unit test could be written as follows:

```python
import pytest


@pytest.mark.parametrize("filename, expected_size", [
    ("image_10x10.jpg", 100),
    ("image_20x25.jpg", 500)
])
def test_AssayImage_init(filename, expected_size):
    # Arrange
    from assay_image import AssayImage
    # Act
    new_instance = AssayImage(filename)
    answer = new_instance.pixel_count
    # Assert
    assert answer == expected_size

```
The `__init__` function is tested by creating an instance of `AssayImage` in 
the unit test.  To ascertain if the calculations done in `__init__` are 
correct, we must access the class properties which were modified to check for
correctness.

## Testing of class methods
Testing of other class methods requires an initial "arrange" step where an
instance of the class is created and is given the initial properties we want
it to have for the various test cases.  Let's look at an example unit test for
the `AssayImage.analyze_image` method.  

```python
@pytest.mark.parametrize("filename, threshold, expected_count", [
    ("image_10x10.jpg", 50, 4),
    ("image_10x10.jpg", 20, 13),
    ("image_20x25.jpg", 50, 18),
    ("image_20x24.jpg", 20, 42)
])
def test_AssayImage_analyze_image(filename, threshold, expected_count):
    # Arrange
    from assay_image import AssayImage
    new_instance = AssayImage(filename)
    # Act
    new_instance.analyze_image(threshold)
    answer = new_instance.anomaly_count
    # Assert
    assert answer == expected_count
```

Since the `analyze_image` method does not return any value for testing, we
need to get the class property/properties that are acted on by the method and
check their values in the assert statement.

The `AssayImage.get_results` method needs a slightly different unit test
format.  It doesn't take any parameters as input, so we will need an additional
step in the Arrange phase to set the class properties as needed for the test.
The method uses the `anomaly_count` and `pixel_count` properties.  So, we need
to first create those values in the class instance before running the method
under test.

```python
@pytest.mark.parametrize("anomaly_count, pixel_count, expected", [
    (30, 100, "Anomalous"),
    (2, 40, "Acceptable")
])
def test_AssayImage_get_results(anomaly_count, pixel_count, expected):
    # Arrange
    from assay_image import AssayImage
    new_instance = AssayImage("image_10x10.jpg")
    new_instance.pixel_count = pixel_count
    new_instance.anomaly_count = anomaly_count
    # Act
    answer = new_instance.get_results()
    # Assert
    assert answer == expected
```

