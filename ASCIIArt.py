import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

# output: used to store result line by line of # 
output = ""

for i in range(h):
    row = input()
    
    for letter in t.upper():
        # use of letter ordinal to find the position in the row
        if 65 <= ord(letter) <= 90:
            output += row[(ord(letter)-65)*l:(ord(letter)-65)*l+l]
        else:
            # if character not alphabetical we use the ? character
            output += row[26*l:27*l]
            
    output += "\n"
    
print(output)
