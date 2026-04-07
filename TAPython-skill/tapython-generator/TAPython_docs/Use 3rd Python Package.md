## Use 3rd Python Package[¶](#use-3rd-python-package)

This guide explains how to use third-party Python packages with TAPython.

## Overview[¶](#overview)

TAPython can use third-party Python packages to extend functionality.

## Installing Packages[¶](#installing-packages)

### Method 1: Using pip[¶](#method-1-using-pip)

Install packages using the Unreal Engine Python:

```
<UE_Python_Path>/python.exe -m pip install <package_name>
```

### Method 2: Site-packages[¶](#method-2-site-packages)

Copy packages to the UE Python site-packages folder:
```
<UE_Engine>/Binaries/ThirdParty/Python3/Win64/Lib/site-packages/
```

## Common Packages[¶](#common-packages)

### Requests[¶](#requests)

HTTP library for web requests:

```python
import requests

response = requests.get("https://api.example.com/data")
```

### NumPy[¶](#numpy)

Numerical computing:

```python
import numpy as np

array = np.array([1, 2, 3])
```

### PIL/Pillow[¶](#pilpillow)

Image processing:

```python
from PIL import Image

img = Image.open("texture.png")
```

##注意事项[¶](#注意事项)

- Ensure packages are compatible with UE Python version
- Avoid packages with C extensions that may not compile
- Test packages in a simple script first

 [Previous](configs_of_tapython.html) [Next](pre-defined_menu_entry.html)
