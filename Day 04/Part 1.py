def search(x, y, grid, vector, order = ["M", "A", "S"]):
    if len(order) == 0:
        return 1

    if x < 0 or x >= len(grid[0]):
        return 0

    if y < 0 or y >= len(grid):
        return 0

    if grid[y][x] != order[0]:
        return 0


    return search(x + vector[0], y + vector[1], grid, vector, order[1:])

grid = [] 

with open("Input.txt") as file:
    grid += [list(line.strip()) for line in file]

total = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "X":
            for vec in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
                total += search(x + vec[0], y + vec[1], grid, vec)

print(total)