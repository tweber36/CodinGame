# Inputs
l, h = [int(i) for i in input().split()]
numeral = [input() for i in range(h)]

# Digits is the list of mayan numbers - list of tuples
digits = []
for d in range(20):
    digits.append(tuple(numeral[line][d*l:d*l+l] for line in range(h)))

# Each number is stored as a list of tuples
n1, n2 = [], []
s1 = int(input())
num_1line = [input() for i in range(s1)]
for d in range(s1//h):
    n1.append(tuple(num_1line[h*d+i] for i in range(h)))

s2 = int(input())
num_2line = [input() for i in range(s2)]
for d in range(s2//h):
    n2.append(tuple(num_2line[h*d+i] for i in range(h)))

operation = input()


def mayan_to_integer(mayan_number, mayan_list):
    """
    Convert a mayan number to an integer
    :param mayan_number: The mayan number as a list of tuples (each tuple is a number from 0 to 19)
    :param mayan_list: The list of mayan numbers from 0 to 19
    :return: an integer
    """
    res, mul, digs = 0, 1, [mayan_list.index(i) for i in mayan_number]
    for i in reversed(digs):
        res += i*mul
        mul *= 20
    return res


def integer_to_mayan(number, mayan_list):
    """
    Convert an integer to its mayan representation
    :param number: Integer
    :param mayan_list: The list of mayan numbers from 0 to 19 (dictionnary)
    :return: A list of tuples representing the number
    """
    digs = [] if number else [0]
    while number:
        digs.append(number % 20)
        number //= 20
    return [mayan_list[i] for i in reversed(digs)]


n1 = mayan_to_integer(n1, digits)
n2 = mayan_to_integer(n2, digits)
result = eval('{}{}{}'.format(n1, '//' if operation == '/' else operation, n2))

for d in integer_to_mayan(result, digits):
    print(*d, sep="\n")
