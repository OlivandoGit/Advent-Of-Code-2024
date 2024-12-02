list1 = []
list2 = []

with open("Input.txt", "r") as file:
    for line in file:
        l1, l2 = line.strip().split()

        list1.append(int(l1))
        list2.append(int(l2))

diffs = []

for i in range(len(list1)):
    l1min = min(list1)
    l2min = min(list2)
    
    diffs.append(abs(l1min - l2min))

    list1.remove(l1min)
    list2.remove(l2min)

print(sum(diffs))