# Boomerang

Constant-like class that allows immutable values. It will always come back the same way.

## Example

```python
import os
from boomerang import constant


config = constant(
    **{
        'ENV': 'test',
        'VERSION': '1.0.0-alpha',
        'BASE_PATH': os.path.abspath('.')
    }
)

config.ENV = 'production' # raises AttributeError
```

## Installation

pip install git+https://github.com/2upmedia/boomerang

## Support

Python 2.7+

## Me
Twitter: @2upmedia
LinkedIn: www.linkedin.com/in/2upmedia
Website: www.2upmedia.com