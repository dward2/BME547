# Issue with Python 3.8 and Jupyter Notebook

In January 2020, when the latest addition of Python (3.8.1) and Jupyter
Notebook (6.0.3) were installed in Windows 10, the Python Kernel would not 
start.  The following fix worked for me.

In your virtual environment, navigate to the following folder:

`venv\Lib\site-packages\tornado\platform`

In this folder, open the file `asyncio.py` for editing.

Look for the following line of code (it was line 32 in my version):
```
from typing import Any, TypeVar, Awaitable, Callable, Union, Optional
```

After that line of code, insert the following lines:
```
# Start BME547 Fix
import sys
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# End BME547 Fix
```

Save the file.

Navigate back to your project folder and try again.