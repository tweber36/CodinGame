import statistics

valuesX = []
valuesY = []
n = int(input())
for i in range(n):
    x, y = [int(i) for i in input().split()]
    valuesX.append(x)
    valuesY.append(y)

median = int(statistics.median(valuesY))

s = sum(abs(y - median) for y in valuesY)

print(s + max(valuesX) - min(valuesX))
