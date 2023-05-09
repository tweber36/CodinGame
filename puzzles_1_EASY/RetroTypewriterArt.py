import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

t = input()

sequences = t.split(" ")
output = ""

special_chars = {
    "sp": " ",
    "bS": "\\",
    "sQ": "'",
}
for elt in sequences:
    if elt.isdigit():
        qty, char = int(elt[:-1]), elt[-1]
        output += qty * char
    elif elt == "nl":
        output += "\n"
    else:
        _, qty, char = re.split("(\\d+)", elt)
        qty = int(qty)
        if char in special_chars:
            char = special_chars[char]
        output += qty * char
print(output)
