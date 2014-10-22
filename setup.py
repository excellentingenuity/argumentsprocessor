from distutils.core import setup
import argumentsprocessor
long_description = ''

try:
    import subprocess
    import pandoc

    process = subprocess.Popen(
        ['which pandoc'],
        shell=True,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    pandoc_path = process.communicate()[0]
    pandoc_path = pandoc_path.strip('\n')

    pandoc.core.PANDOC_PATH = pandoc_path

    doc = pandoc.Document()
    doc.markdown = open('README.md').read()

    long_description = doc.rst
    #converts markdown readme to reStructured
    z = pypandoc.convert('README','rst',format='markdown')

    #writes converted file
    with open('README.rst','w') as outfile:
        outfile.write(z)

    #converts markdown license to reStructured
    z = pypandoc.convert('LICENSE','rst',format='markdown')

    #writes converted file
    with open('LICENSE.rst','w') as outfile:
        outfile.write(z)
except:
    pass
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
