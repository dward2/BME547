# Sphinx Documentation

[Sphinx](http://sphinx-doc.org/) is a documentation generation engine for 
Python that is extremely powerful and has lots of configuration options.  

Here are steps to automatically generate API-like documentation using 
docstrings in either reStructuredText, Google, or Numpy format.

**Note:** The instructions given below may very  from that found in 
the Sphinx documentation.  The instructions below are written to put
all of the Sphinx files into a subfolder called `docs` in your project folder.

1. Navigate to the root folder containing your project files.

1. Ensure that `sphinx` is installed in your virtual environment and that the
virtual environment is active.

1. At the command line, enter :  
  ``sphinx-quickstart docs``  
  You will be given the opportunity to enter some information about the
  project.  When defaults are available, select the default.  
  When finished, a subdirectory (``docs``) will be created that will contain 
    the Sphinx-generated files.

1. In the `docs` directory, there is a file called `conf.py`.  The following
   edits need to be made to this file and then saved:
   + You will see the following lines that are commented out:    
        ```
        # import os
        # import sys
        # sys.path.insert(0, os.path.abspath('.'))
        ```  
        Remove the comment markers and change the path from `'.'` to `'..'` so 
        that the lines now look as follows:
        ```
        import os
        import sys
        sys.path.insert(0, os.path.abspath('..'))
        ```
   + Modify the `extensions` variable to include `sphinx.ext.autodoc`:
       ```
       extensions = [
       'sphinx.ext.autodoc'
       ]
       ```
   + If using Google- or Numpy-style docstrings, further modify the 
   `extensions` variable to include `sphinx.ext.napoleon`:
       ```
       extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.napoleon'
       ]
       ```
       
1. Back on the command line, while still in the root folder containing your 
project files, enter the following command:  
  -- For reStructuredText docstrings:  `sphinx-apidoc -o docs .`  
  -- For Google- or Numpy-style docstrings:  `sphinx-apidoc -f -o docs .`  
  This will sweep through all of the `*.py` files in your root directory and 
  create corresponding `*.rst` files in the `docs` folder.
  
1. In the `docs` folder, edit the `index.rst` file to include the module files
that should be included in the documentation.  These are the `*.rst` files
created above.  Look for the lines that start with `.. toctree::` and include
the list of `*.rst` files after these lines with a blank line in between.  Do
not include the `.rst` extension.  For example:  
    ```
    .. toctree::
       :maxdepth: 2
       :caption: Contents:
   
       module1
       module2
    ```
  
    * Make sure to indent your file entries in the `index.rst` the same as the 
    lines above!! Failure to indent will cause the rst-parser to "miss" your 
    files.
 
1. Switch into the `docs` directory using the command `cd docs`.  In the `docs`
folder, enter the following command:  
    ```
    sphinx-build -M html . _build
    ```
    This will create a folder called `docs/_build/html` which contains the 
    generated html documentation pages, with the default webpage being 
    `index.html`.

**Example:** https://mlp6.github.io/fem/

Relevant GitHub documentation: https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-your-github-pages-site-from-a-docs-folder-on-your-master-branch


Documentation for [Napleon](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
extension in Sphinx for Google or Numpy style docstrings: 
 http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
 
 ### Additional documentation in Sphinx
 The instructions above generate information using the docstrings found in the
 Python code.  To add additional webpages to the Sphinx-generated
 documentation beyond what is in the docstrings and Python modules, do the 
 following:
 
 * In the folder `docs`, create a file with the extension `.rst` (example:
 `api.rst`).
 * Using restructured text, add the content to this file.
   + Here is a good cheat sheet for ReStructured Text, although Sphinx doesn't
   seem to recognize all of these formats: <http://docutils.sourceforge.net/docs/user/rst/quickref.html>
   + Example:  
   ```
   API Module
   ==========

    Add a patient
    -------------
    
    ::
    
      POST  URL/new_patient
    
    This route takes a dictionary with the following information.
    
    **patient_id**
      The id number of the patient.  
    **age**
      The age of the patient.
    **attending_email**
      The e-mail of the attending physician
      
      
    Add a heart rate to a patient record
    ------------------------------------
    
    ::
    
      POST URL/add_heart_rate
    
    This route takes a dictionary with the following informaiton.
    
    patient_id
      The id number of the patient to which to add a heart rate.
    
    heart_rate
      The heart rate to be added.
    ```
* In the `index.rst` file in the `docs` folder, add the name of this newly
created file, without the `.rst` extension, to the file list as shown in this
example:
  ```
    .. toctree::
       :maxdepth: 2
       :caption: Contents:
   
       api
       module1
       module2
  ```