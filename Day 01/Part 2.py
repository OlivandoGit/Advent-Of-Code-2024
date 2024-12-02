list1 = []
list2 = []

with open("Input.txt", "r") as file:
    for line in file:
        l1, l2 = line.strip().split()

        list1.append(int(l1))
        list2.append(int(l2))

list2count = {}

for num in list2:
    if num not in list2count.keys():
        list2count[num] = 1

    else: 
        list2count[num] = list2count[num] + 1

total = 0

for num in list1:
    if num in list2count.keys():
        total += num * list2count[num]

print(total)