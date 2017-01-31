n = int(input())  # the number of relationships of influence
influences = [input().split() for i in range(n)]

length = 0
people_left = {x for (x, _) in influences}

while len(people_left) > 0:
    people_left = {y for (x, y) in influences if x in people_left}
    length += 1

print(length)
