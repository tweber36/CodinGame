import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mime_dict = {}


for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_dict[ext.lower()] = mt
    
pattern = re.compile(r'')

for i in range(q):
    fname = input()  # One file name per line.
    if pattern.search(fname.lower()):
        extension = pattern.split(fname)[-1].lower()
        if extension in mime_dict.keys():
            print(mime_dict[extension])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
