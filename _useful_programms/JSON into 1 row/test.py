import json
import re

with open('test.json') as handle:
    for line in handle:
        newline = re.sub("[\n]","\\\\n",line)
        newline = re.sub("[\t]","\\\\t",newline)
        with open('somefile.txt', 'a') as the_file:
            the_file.write(newline)