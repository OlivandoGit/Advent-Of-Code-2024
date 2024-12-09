grid = []

with open("Input.txt") as file:
    grid = [list(line.strip()) for line in file]

ants = {}

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == ".":
            continue

        if char not in ants.keys():
            ants[char] = [(x, y)]

        else:
            ants[char] = ants[char] + [(x, y)]

antinodes = set()

for freq in ants.keys():
    for i, coords in enumerate(ants[freq]):
        for coords2 in ants[freq][:i] + ants[freq][i + 1:]:
            
            dx = coords[0] - coords2[0]
            dy = coords[1] - coords2[1]

            if coords[0] + dx < 0 or coords[0] + dx >= len(grid[0]):
                continue

            if coords[1] + dy < 0 or coords[1] + dy >= len(grid):
                continue

            antinodes.add((coords[0] + dx, coords[1] + dy))


print(len(antinodes))