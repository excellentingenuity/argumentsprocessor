from distutils.core import setup
import argumentsprocessor
long_description = open('README.rst').read()

setup(
  name = 'argumentsprocessor',
  packages = ['argumentsprocessor'], # this must be the same as the name above
  version = argumentsprocessor.__version__,
  description = 'A Python module that process a dictionary of arguments against a supplied dictionary of expected arguments.',
  long_description=long_description,
  author = 'James Johnson',
  author_email = 'james.johnson@excellentingenuity.com',
  url = 'https://github.com/excellentingenuity/argumentsprocessor', # use the URL to the github repo
  download_url = 'https://github.com/excellentingenuity/argumentsprocessor.git', # I'll explain this in a second
  keywords = ['arguments', 'processing'], # arbitrary keywords
  license = 'BSD New',
  classifiers = [
    'Programming Language :: Python :: 3.4',
    'License :: OSI Approved :: BSD License',
    'Development Status :: 5 - Production/Stable',
  ],
)
