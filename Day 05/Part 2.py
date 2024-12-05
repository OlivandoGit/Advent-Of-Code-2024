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

valid = []

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
        valid.append(update)

invalid = [update for update in updates if update not in valid]

total = 0

for update in invalid:
    corrected = [update[0]]
    
    for page in update[1:]:
        if page not in rules.keys():
            corrected.append(page)
            continue

        lowest = len(update)
        for page2 in rules[page]:
            if page2 in corrected and corrected.index(page2) < lowest:
                lowest = corrected.index(page2)

        corrected.insert(lowest, page)

    total += corrected[len(corrected) // 2]

print(total)