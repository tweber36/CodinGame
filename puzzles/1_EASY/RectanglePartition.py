from collections import Counter

w, h, count_x, count_y = [int(i) for i in input().split()]
x_coords = [0]
y_coords = [0]
for i in input().split():
    x = int(i)
    x_coords.append(x)
x_coords.append(w)
for i in input().split():
    y = int(i)
    y_coords.append(y)
y_coords.append(h)

nb_squares = 0

diffs_x = []
diffs_y = []
for i, x in enumerate(x_coords):
    if i == len(x_coords) - 1:
        break

    for j, x_2 in enumerate(x_coords[i + 1:]):
        diffs_x.append(x_2 - x)

for i, y in enumerate(y_coords):
    if i == len(y_coords) - 1:
        break

    for j, y_2 in enumerate(y_coords[i + 1:]):
        diffs_y.append(y_2 - y)

x_counts = Counter(diffs_x)
y_counts = Counter(diffs_y)

nb_squares = sum(x_counts[i]*y_counts[i] for i in range(max(w+1, h+1)))

print(nb_squares)
