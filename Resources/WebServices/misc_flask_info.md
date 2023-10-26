# Miscellaneous Info on Flask

## JSON Settings and Dictionaries
Flask uses the Python `json` package for encoding data into strings for 
responses.  

The `json` package, when encoding dictionaries, will not sort the keys but
rather keep them in insertion order.  But, it can be set to sort the keys
using the `sort_keys` named parameter.  See 
<https://docs.python.org/3/library/json.html#json.dumps>

The Flask implementation (as of 10/26/2023) sets this `sort_keys` to `True`
when using `jsonify`.  See 
<https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.provider.DefaultJSONProvider.sort_keys>.

To change the behavior used by Flask, you can change the value of the 
`sort_keys` parameter as follows:

```python
app = Flask(__name__)
app.json.sort_keys = False
```