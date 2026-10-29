# Unit Testing of Functions That Make Server Requests

If a function makes a GET or POST request to a server, it is often hard to 
unit test that function using `pytest` because the response from the server
may be uncertain.  For example, the server may not be accessible.  So, it is 
often desirable to "mock" the response that is obtained by the server request.

The package [`requests-mock`](https://requests-mock.readthedocs.io/en/latest/)
provides mocking functionality for requests.  To use this package, install
`requests-mock` in your virtual environment.  

Let's look at an example.

Assume you have a function that you want to test that looks like this:

```python
# my_client.py

server = "http://127.0.0.1:5000"

def get_info_from_server(customer_id):
    r = requests.get(server + "/get_customer/{}".format(customer_id))
    if r.status_code == 400:
        return "Unknown customer"
    customer_info = r.json()
    if customer_info["age"] < 15:
        return "Send toy catalog"
    else:
        return "Send clothing catalog"
```

Here is what the unit test function would look like:
```python
# test_my_client.py

import requests_mock

def test_get_info_from_server(requests_mock):
    # Arrange
    from my_client import get_info_from_server, server
    requests_mock.get(server + "/get_customer/123",
                      status_code=200,
                      json={"age": 21}
                      )
    expected = "Send clothing catalog"
    # Act
    answer = get_info_from_server(123)
    # Assert
    assert answer == expected
```

First, `requests_mock` must be imported.  Then, `requests_mock` must be 
included as the last parameter in the function definition.  Inside the unit
test function, we need to tell `requests_mock` what request to provide a mock
response for.  We do that with the `requests_mock.get` command.  If we wanted
to mock a POST request, we would use the `requests_mock.post` command.

The first parameter to pass to `requests_mock.get` is the URL to mock.  Since
we want to give it the exact URL needed, we import the `server` variable to use.

The remaining inputs are named parameters.  
* `status_code` indicates what status code should be returned by the mock 
  request.  
* `json` is a Python variable or value that will be returned as a JSON encoded 
  string with the mock request.
* `text` (not used) would indicate what text string should be returned as part
  of the response.  

In the example above, we are mocking a response for a successful post (status 
code of 200) with the JSON return variable being a dictionary with an age of 21.

The rest of the unit test function follows the usual testing approach.