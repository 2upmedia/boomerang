from distutils.core import setup
import sys


if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    print('Sorry, Python < 2.7 is not supported')
    sys.exit(1)

setup(
    name='boomerang',
    version='0.1.0',
    packages=[''],
    url='http://www.github.com/2upmedia/boomerang',
    license='MIT',
    author='Jorge Colon, 2UP Media',
    author_email='jorge@2upmedia.com',
    description='Constant-like class that allows immutable values. It will always come back the same way.'
)
