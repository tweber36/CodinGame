import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())

data = []
lon = math.radians(float(lon.replace(",", ".")))
lat = math.radians(float(lat.replace(",", ".")))
dist_min = 6371

for i in range(n):
    defib = input()
    data.append(re.split(r';', defib))

    lon_i = math.radians(float(data[i][4].replace(",", ".")))
    lat_i = math.radians(float(data[i][5].replace(",", ".")))
    
    x = (lon_i - lon) * math.cos((lat + lat_i) / 2)
    y = (lat_i - lat)
    d = math.sqrt(x**2 + y**2) * 6371
    
    if d <= dist_min:
        dist_min = d
        index = i

print(data[index][1])
