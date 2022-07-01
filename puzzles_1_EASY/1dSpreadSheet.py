# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def get_value(values, line):
    if str(values[line][1]).startswith('$'):
        values[line][1] = get_value(values, int(values[line][1][1:]))
    if str(values[line][2]).startswith('$'):
        values[line][2] = get_value(values, int(values[line][2][1:]))
    if values[line][2] == '_':
        values[line][2] = 0

    values[line][1] = int(values[line][1])
    values[line][2] = int(values[line][2])
    if values[line][0] == 'VALUE':
        return values[line][1]
    elif values[line][0] == 'ADD':
        return values[line][1] + values[line][2]
    elif values[line][0] == 'SUB':
        return values[line][1] - values[line][2]
    elif values[line][0] == 'MULT':
        return values[line][1] * values[line][2]


n = int(input())
values = []
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    values.append([operation, arg_1, arg_2])

for i in range(n):
    print(get_value(values, i))
