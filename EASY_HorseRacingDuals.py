import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
strengths = []

diff_min = 10000000

for i in range(n):
    pi = int(input())
    strengths.append(pi)
    
strengths.sort(reverse=True)

diffs = [strengths[i] - strengths[i+1] for i in range(n-1)]
print(min(diffs))
    