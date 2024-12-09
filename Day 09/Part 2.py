layout = ""

with open("Input.txt") as file:
    layout = [int(x) for x in file.readline().strip()]

data = []
empty = []

fileid = 0
for i, num in enumerate(layout):
    if i % 2 == 0:
        data.append([fileid, num])
        fileid += 1

    else:
        empty.append([[], num])

for i, file in enumerate(data[::-1]):
    fileid, size = file
    
    for j, e in enumerate(empty[:len(data) - 1 - i]):
        if e[1] >= size:

            empty[j][0].append((file))
            empty[j][1] -= size

            data[len(data) - 1 - i] = (None, size)

            break

total = 0
pos = 0

for i, dat in enumerate(data):
    for j in range(dat[1]):
        total += (dat[0] or 0) * pos
        pos += 1

    if i >= len(empty):
        continue

    for emp in empty[i][0]:
        for e in range(emp[1]):
            total += emp[0] * pos
            pos += 1

    pos += empty[i][1]

print(total)
