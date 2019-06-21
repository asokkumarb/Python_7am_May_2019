"""
# What is OS.walk?

It generates the file names in a directory tree by walking the tree either
top-down or bottom-up.

For each directory in the tree rooted at directory top (including top itself), 
it yields a 3-tuple (dirpath, dirnames, filenames).

1. dirpath	# is a string, the path to the directory. 

2. dirnames	# is a list of the names of the subdirectories in dirpath
		  (excluding '.' and '..'). 

3. filenames	# is a list of the names of the non-directory files in dirpath. 


What is fnmatch?

The fnmatch module compares file names against glob-style patterns such as used
by Unix/Linux shells.

These are not the same as the more sophisticated regular expression rules. 

Its purely a string matching operation. 

If you find it more convenient to use a different pattern style, for example 
regular expressions, then simply use regex operations to match your filenames.

"""

# Find all mp3 files in my PC/Laptop

import os
import fnmatch

path = '/Users/keshavkummari/Python_7am_May_2019/File_and_Dir/'
pattern = "*.mp3"

for root,dirs,files in os.walk(path):
    for filename in fnmatch.filter(files,pattern):
        print(os.path.join(root,filename))

# Search Computer for Specific files

Example : .jpg , .jpeg , .png .tif .tiff