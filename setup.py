from distutils.core import setup
import sys


if sys.version_info.major == 2 and sys.version_info.minor < 7:
    print 'Sorry, Python < 2.7 is not supported'
    sys.exit(1)

setup(
    name='boomerang',
    version='0.1.0',
    packages=[''],
    url='http://www.github.com/2upmedia/boomerang',
    license='MIT',
    author='Jorge Colon, 2UP Media',
    author_email='jorge@2upmedia.com',
    description='Constant-like class'
)
