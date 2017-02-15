from itertools import groupby

n = int(input())
phone_numbers = sorted(input() for _ in range(n))


def calculate_elements(numbers):
    """
    Recursive function to calculate the numbers of elements necessary to store a list of numbers.

    If there is only 1 number, it returns the length of the number
    Otherwise, it groups numbers by their first number because we need to store it only once
    Then send a recursive call with a sub-list of each group without the first number
    (until there's only one number left in the sub-list)
    :param numbers: A list of numbers - but string format !
    :return: The count of elements necessary to store all the numbers following the implementation given.
    """
    if len(numbers) == 1:
        return len(numbers[0])

    count = 0

    for value, group in groupby(numbers, key=lambda x: x[0]):
        count += 1
        new_numbers = sorted(p[1:] for p in group if len(p) > 1)
        count += calculate_elements(new_numbers)

    return count

print(calculate_elements(phone_numbers))
