# iwc_client.py
# Client for calling Ideal Weight Calculator Server
# David Ward, March 2019

import requests

# Check to see if server is on
print("Checking if server is on by accessing '/' route")
r = requests.get("http://127.0.0.1:5000/")
print("'r' type is {}".format(type(r)))
print("'r' = {}".format(r))
print("'r.text' type is {}".format(type(r.text)))
print("'r.text' = {}".format(r.text))

# Get information from server
print("Making a GET request to '/info' route")
r = requests.get("http://127.0.0.1:5000/info")
print("'r' type is {}".format(type(r)))
print("'r' = {}".format(r))
print("'r.text' type is {}".format(type(r.text)))
print("'r.text' = {}".format(r.text))
print("'r.json()' type is {}".format(type(r.json())))
print("'r.json() = {}'".format(r.json()))

# Ask server to calculate ideal weight
print("Asking server to calculate ideal weight")
patient_data = {
                "age": 43,
                "height_in":  52,
                "gender": "female"
               }
r = requests.post("http://127.0.0.1:5000/calculate_iwc", json=patient_data)
print("'r' = {}".format(r))
print("'r.json() = {}".format(r.json()))
