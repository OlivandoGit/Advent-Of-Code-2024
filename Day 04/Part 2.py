grid = [] 

with open("Input.txt") as file:
    grid += [list(line.strip()) for line in file]

search = ["M", "S"]
total = 0

for y, line in enumerate(grid):
    if y == 0 or y == len(grid) - 1:
        continue

    for x, char in enumerate(line):
        if x == 0 or x == len(line) - 1:
            continue

        if char != "A":
            continue

        if grid[y - 1][x - 1] in search and grid[y + 1][x + 1] in [s for s in search if s != grid[y - 1][x - 1]]:
            if grid[y - 1][x + 1] in search and grid[y + 1][x - 1] in [s for s in search if s != grid[y - 1][x + 1]]:
                total += 1

print(total)
