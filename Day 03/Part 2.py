memory = []

with open("Input.txt", "r") as file:
    for line in file:
        memory.append(line.strip())

memory = "".join(memory)

memory = memory.split("mul(")

total = 0

for j, line in enumerate(memory):
    for i, char in enumerate(line):
        previous = "".join(memory[0:j])[::-1]

        if ")(t'nod" in previous:
            if ")(od" not in previous:
                break

            if previous.index(")(t'nod") < previous.index(")(od"):
                break

        if not char.isdigit() and char not in [",", ")"]:
            break

        elif char != ")":
            continue

        if "," in line[0:i]:
            nums = [int(x) for x in line[0:i].split(",")]
            
            if len(nums) != 2:
                break

            total += nums[0] * nums[1]
            break

print(total)