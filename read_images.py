import re
import os
from fnmatch import fnmatch

def walk(folder):
    for dirpath, dirnames, files in os.walk(folder):
        print(f"##################\n{dirpath}\n##################")
        curr_family = re.split('/|\\\\', dirpath)[-1]
        for file in files:
            if fnmatch(file, "*.pdf"):
                continue