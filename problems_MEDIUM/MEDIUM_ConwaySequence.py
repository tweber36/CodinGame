from itertools import groupby

r = [int(input())]
l = int(input())


def next_row(row):
    for value, lst in groupby(row):
        yield sum(1 for _ in lst)
        yield value

for i in range(l-1):
    r = next_row(r)

print(*r)
