def to_binary(s: str):
    s = s.replace("-", "1").replace("_", "0")
    return int(s, 2)


def to_text(n: int, text_length: int, invert=False):
    result = bin(n)[2:]
    result = "0" * (text_length - len(result)) + result
    if invert:
        return result.replace("0", "-").replace("1", "_")
    else:
        return result.replace("0", "_").replace("1", "-")


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())
inputs = {}
outputs = []
for i in range(n):
    input_name, input_signal = input().split()
    inputs[input_name] = input_signal
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()

    if _type in ["AND", "NAND"]:
        result = to_binary(inputs[input_name_1]) & to_binary(inputs[input_name_2])
    elif _type in ["OR", "NOR"]:
        result = to_binary(inputs[input_name_1]) | to_binary(inputs[input_name_2])
    elif _type in ["XOR", "NXOR"]:
        result = to_binary(inputs[input_name_1]) ^ to_binary(inputs[input_name_2])

    if _type in ["NAND", "NOR", "NXOR"]:
        print(output_name, to_text(result, len(inputs[input_name_1]), invert=True))
    else:
        print(output_name, to_text(result, len(inputs[input_name_1])))
