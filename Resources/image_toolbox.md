# Image Handling Toolbox

### Convert image file to base64 string
```python
with open(filename, "rb") as image_file:
    b64_bytes = base64.b64encode(image_file.read())
z = str(b64_bytes, encoding='utf-8')
```