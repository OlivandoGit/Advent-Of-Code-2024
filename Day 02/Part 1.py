reports = []

with open("Input.txt", "r") as file:
    for line in file:
        reports.append([int(x) for x in line.strip().split()])

total = 0

for report in reports:
    asc = all([x < y for x, y in zip(report, report[1:])])
    desc = all([x > y for x, y in zip(report, report[1:])])

    if not (asc or desc):
        continue

    safe = all([abs(x - y) <= 3 for x, y in zip(report, report[1:])])

    if safe:
        total += 1

print(total)