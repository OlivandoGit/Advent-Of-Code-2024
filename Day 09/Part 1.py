layout = ""

with open("Input.txt") as file:
    layout = [int(x) for x in file.readline().strip()]

memory = []

id = 0
for i, num in enumerate(layout):
    if i % 2 == 0:
        memory += [id for i in range(num)]
        id += 1

    else:
        memory += [None for i in range(num)]

left = 0
right = len(memory) - 1

while left < right:
    while memory[left] != None:
        left += 1

    while memory[right] == None:
        right -= 1

    if left < right:
        memory[left] = memory[right]
        memory[right] = None

total = 0

for i, num in enumerate(memory):
    if num != None:
        total += i * num

print(total)