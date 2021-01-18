# Web Interface with Flask

Up to this point in the class, we have generally been using our server
primarily as a "back-end" system.  Our routes have received data, manipulated
that data, and then returned the data.  Any I/O was done by a client program.

Flask can also be used for "front-end" web development.  In this case, the
server creates and displays web pages that the user can interact with, enter
data to be sent to the server, and the see the results of any server
output.

## `render_template`
Flask provides the `render_template` function that, when used in conjunction
with the `return` command, will display the webpage defined by a template.

Here is a very short example.  Let's say we have an HTML document called
`index.html` that we want to display at the base route "\".  In our project
directory, we create a subfolder called `templates`.  In that fo
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

```
First, the `render_template` function must be imported from `flask`.  Then, the
flask handler function should end with a call to 
`return render_template("index.html")`.  The name of the html file to display
is included as a string parameter.  Flask will look for this file in the
`templates` folder created above.

