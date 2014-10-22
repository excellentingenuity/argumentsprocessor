#!/usr/bin/env python

import pandoc
import subprocess
import os


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
f = open('README.txt','w+')
f.write(doc.rst)
f.close()

docl = pandoc.Document()
docl.markdown = open('LICENSE.md').read()
fl = open('LICENSE.txt','w+')
fl.write(docl.rst)
fl.close()

