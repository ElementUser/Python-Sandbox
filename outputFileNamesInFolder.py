###################################################
# Outputs all file names in the current folder
###################################################

import os, sys

path = sys.path[0]
for filename_dir in os.listdir(path):
     filename, ext = os.path.splitext(filename_dir)
     if ext == '.upk':
         print('decompress.exe -lzo ' + '"' + filename + ext + '"')