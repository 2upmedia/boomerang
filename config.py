import os
from boomerang import constant

config = constant(
    **{
        'ENV': 'test',
        'VERSION': '1.0.0-alpha',
        'BASE_PATH': os.path.abspath('.')
    }
)