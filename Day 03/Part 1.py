memory = []

with open("Test.txt", "r") as file:
    for line in file:
        memory.append(line.strip())

memory = "".join(memory)

memory = memory.split("mul(")

total = 0

for line in memory:
    for i, char in enumerate(line):
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