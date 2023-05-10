import string

LETTERS = string.ascii_uppercase

operation = input()
pseudo_random_number = int(input())
rotors = []
for i in range(3):
    rotors.append(input())
message = input()


def caesar_shift(message: str, starting_number: int, operation: str) -> str:
    result = ""
    for idx, char in enumerate(message):
        if operation == "ENCODE":
            result += LETTERS[(LETTERS.index(char) + starting_number + idx) % 26]
        elif operation == "DECODE":
            result += LETTERS[(LETTERS.index(char) - starting_number - idx) % 26]
    return result


def apply_rotor(message: str, rotor: str, operation: str) -> str:
    if operation == "ENCODE":
        return "".join(rotor[LETTERS.index(c)] for c in message)
    elif operation == "DECODE":
        return "".join(LETTERS[rotor.index(c)] for c in message)


if operation == "ENCODE":
    message = caesar_shift(message, pseudo_random_number, operation)
    for rotor in rotors:
        message = apply_rotor(message, rotor, operation)
elif operation == "DECODE":
    for rotor in reversed(rotors):
        message = apply_rotor(message, rotor, operation)
    message = caesar_shift(message, pseudo_random_number, operation)
print(message)
