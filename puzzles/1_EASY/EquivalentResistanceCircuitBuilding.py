from typing import List, Tuple


def get_subgroup(circuit: List, idx: int) -> Tuple[List, str]:
    matching_symbol = 1
    if circuit[idx] == "(":
        for i, elt in enumerate(circuit[idx + 1:]):
            if elt == "(":
                matching_symbol += 1
            elif elt == ")":
                matching_symbol -= 1
            if matching_symbol == 0:
                break
        return circuit[idx + 1: idx + 1 + i], "series"
    elif circuit[idx] == "[":
        for i, elt in enumerate(circuit[idx + 1:]):
            if elt == "[":
                matching_symbol += 1
            elif elt == "]":
                matching_symbol -= 1
            if matching_symbol == 0:
                break
        return circuit[idx + 1: idx + 1 + i], "parallel"


def get_eq_rev(circuit: List, type: str) -> float:
    elements = []
    i = 0
    while i < len(circuit):
        if circuit[i] in "([":
            subgroup, subtype = get_subgroup(circuit, i)
            elements.append(get_eq_rev(subgroup, type=subtype))
            i += len(subgroup) + 2
        else:
            elements.append(values[circuit[i]])
            i += 1
    if type == "series":
        return sum(elements)
    elif type == "parallel":
        return 1 / sum(1 / x for x in elements)


n = int(input())
values = {}
for i in range(n):
    inputs = input().split()
    values[inputs[0]] = int(inputs[1])
circuit = input().split()

if circuit[0] == "(":
    result = get_eq_rev(circuit[1:-1], type="series")
elif circuit[0] == "[":
    result = get_eq_rev(circuit[1:-1], type="parallel")

print(f"{result:.1f}")
