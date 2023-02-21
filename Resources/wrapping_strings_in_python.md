# Wrapping Strings In Python

The PEP-8 standard specifies a maximum line length of 79 characters.  There
are times when a string is long enough to require more than that number of
spaces on a line.  In this case, the string must be defined across multiple
lines of text.

Python will concatenate two strings that are adjacent.  For example:
```python
output_string = "Hello" "there."
print(output_string)
```
will yield this output:
```
Hellothere.
```

Note that Python will not insert a space or other delimiter between the strings
so any needed delimiters in the final string need to be included in one of the
original strings.  

This concatenation of strings cn be used across multiple lines by the use of 
the `\` continuation symbol as shown here:
```python
my_string = "This is a really long string I want to split across " \
            "multiple lines."
```
The `\` symbol tells Python to treat the next line as a continuation of the
current line.  So, `my_string` will be a concatenation of the two strings on
different lines.

If the string is being defined within enclosing characters, such as `()`, `[]`,
or `{}`, the continuation symbol is not required as Python will automatically
look to the next line if the closing symbol is not found.  For example:

```python
my_string = ["This is a really long string i want to split "
             "across multiple lines."]
```
