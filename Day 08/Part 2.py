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

            newx = coords[0]
            newy = coords[1]

            while newx >= 0 and newx < len(grid[0]) and newy >= 0 and newy < len(grid):
                antinodes.add((newx, newy))    

                newx += dx
                newy += dy          

print(len(antinodes))