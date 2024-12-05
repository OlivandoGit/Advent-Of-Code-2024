rules = {}
updates = []

with open("Input.txt") as file:
    for line in file:
        if "|" in line:
            p1, p2 = line.strip().split("|")

            p1 = int(p1)
            p2 = int(p2)
            
            if p1 in rules.keys():
                rules[p1].append(p2)

            else:
                rules[p1] = [p2]

        elif line != "\n":
            updates.append([int(x) for x in line.strip().split(",")])

total = 0
for update in updates:
    for page in update:
        if page not in rules.keys():
            continue

        for page2 in rules[page]:
            if page2 in update and update.index(page2) < update.index(page):
                break

        else:
            continue

        break
    
    else:
        total += update[len(update) // 2]

print(total)