import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

if n == 0:
    print(0)
else:
    temperatures = [int(t) for t in temps.split(' ')]
    temperatures_abs = [abs(t) for t in temperatures]

    temperature_min = min(temperatures_abs)
    if temperature_min in temperatures:
        print(temperature_min)
    else:
        print("-" + str(temperature_min))
