from distutils.core import setup
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

except:
    pass
setup(
  name = 'argumentsprocessor',
  packages = ['argumentsprocessor'], # this must be the same as the name above
  version = '1.0.4',
  description = 'An arguments processor',
  long_description=long_description,
  author = 'James Johnson',
  author_email = 'james.johnson@excellentingenuity.com',
  url = 'https://github.com/excellentingenuity/argumentsprocessor', # use the URL to the github repo
  download_url = 'https://github.com/excellentingenuity/argumentsprocessor.git', # I'll explain this in a second
  keywords = ['arguments', 'processing'], # arbitrary keywords
  license = 'BSD New',
  classifiers = [
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'License :: OSI Approved :: BSD License',
    'Development Status :: 5 - Production/Stable',
  ],
)
