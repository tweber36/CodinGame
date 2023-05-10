w, h = [int(i) for i in input().split()]
links = {}

input_labels = input().split()
for i in range(h - 2):
    line = input().split("|")[1:-1]
    for j, elt in enumerate(line):
        if elt == "--":
            links[(i, j)] = j + 1
            links[(i, j + 1)] = j
output_labels = input().split()

for starting_col in range((w - 1) // 3 + 1):
    col = starting_col
    for row in range(h-2):
        col = links.get((row, col), col)
    print(input_labels[starting_col] + output_labels[col])
