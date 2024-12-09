def permutate(expected, values):
    if values[0] > expected:
        return False

    if len(values) == 1:
        return values[0] == expected

    if permutate(expected, [values[0] + values[1]] + values[2:]):
        return True

    if permutate(expected, [values[0] * values[1]] + values[2:]):
        return True

    if permutate(expected, [int(str(values[0]) + str(values[1]))] + values[2:]):
        return True

    return False


calcs = []

with open("Input.txt") as file:
    calcs = [line.strip().split() for line in file]

total = 0

for i, calc in enumerate(calcs):
    expected = int(calc[0].strip(":"))
    
    
    if permutate(expected, [int(x) for x in calc[1:]]):
        total += expected

print(total)

