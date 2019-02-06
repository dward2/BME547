# Sphinx Documentation

[Sphinx](http://sphinx-doc.org/) is a documentation generation engine for Python
that is extremely powerful and lots of configuration options.  Here's a quick
start to automatically generate API-like documentation using docstrings in 
reStructuredText format.
(For Google or Numpy docstring formats, see modified instructions in the 
Napoleon section at bottom of page.)

1. ``sphinx-quickstart docs``  
    This will create a distinct subdirectory (``docs/``) that contains all
documentation.

1. There are lots of options that you will be walked through... defaults are
   usually okay, but be sure to select 'y' for the ``autodoc`` option.
1. add path to ``docs/conf.py``:  
    ```
    sys.path.insert(0, os.path.abspath('..'))
    ```    
    There is a similar path commented out near the header that you can uncomment
and edit, along with the 2 import statements of the `os` and `sys` modules.
1. Run `sphinx-apidoc -o docs .` from the root level of your project (this
   will sweep through all of the `*.py` files in `.` and create
   corresponding `*.rst` files in `docs/`)
1. `docs/index.rst` -> add modules that you'd like included in the documentation  
    * Make sure that your docstring have a blank link before the rst `:param:` and
    `:returns:` lines.
    * Make sure to indent your file entries!!  Failure to indent will cause the
    rst-parser to "miss" your files.
    * You may want to add `_build/` to your `.gitignore` files:
1. Run Makefile to generate documentation (e.g., ``make html``).  This will
   create `docs/_build/html` with the default webpage being `index.html`.

**Example:** https://mlp6.github.io/fem/

Relevant GitHub documentation: https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/#publishing-your-github-pages-site-from-a-docs-folder-on-your-master-branch

## Google or Numpy Docstrings
To use sphinx with Google or Numpy style docstrings, use the [Napleon](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) extension.  Follow the instructions above with 
the following additions/changes:

When editing the `docs/conf.py` file, include the napoleon extension as follows:
```
# Add napoleon to the extensions list
extensions = ['sphinx.ext.napoleon']
```
When running the `sphinx-apidoc` command, the options are somewhat different:
```
sphinx-apidoc -f -o docs .
```
Visit http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html for full documentation on Napoleon.