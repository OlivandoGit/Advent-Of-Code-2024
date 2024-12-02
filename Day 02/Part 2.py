def test(report):
    asc = all([x < y for x, y in zip(report, report[1:])])
    desc = all([x > y for x, y in zip(report, report[1:])])
    safe = all([abs(x - y) <= 3 for x, y in zip(report, report[1:])])

    return (asc or desc) and safe

reports = []

with open("Input.txt", "r") as file:
    for line in file:
        reports.append([int(x) for x in line.strip().split()])

total = 0

for report in reports:
    if test(report):
        total += 1
        continue

    for i in range(len(report)):
        if test(report[:i] + report[i + 1 :]):
            total += 1
            break

print(total)