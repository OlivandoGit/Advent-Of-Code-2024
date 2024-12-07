def checkloop(coords, direction, board):
    visited = set()

    while coords[0] >= 0 and coords[0] < len(board[0]) and coords[1] >=0 and coords[1] < len(board):   
        if (coords, direction) in visited:
            return True

        if board[coords[1]][coords[0]] == "#":
            coords = (coords[0] + (direction[0] * -1), coords[1] + (direction[1] * -1))

            if direction == (0, -1):
                direction = (1, 0)

            elif direction == (1, 0):
                direction = (0, 1)

            elif direction == (0, 1):
                direction = (-1, 0)

            elif direction == (-1, 0):
                direction = (0, -1)

        else:
            board[coords[1]][coords[0]] = "X"
            visited.add((coords, direction))
        
        coords = (coords[0] + direction[0], coords[1] + direction[1])
    
    return False

board = []

with open("Input.txt") as file:
    board += [list(line.strip()) for line in file]

start = (0, 0)

for y, line in enumerate(board):
    for x, char in enumerate(line):
        if char == "^":
            start = (x, y)
            break
    else:
        continue

    break

coords = start
direction = (0, -1)
visited = []

while coords[0] >= 0 and coords[0] < len(board[0]) and coords[1] >=0 and coords[1] < len(board):   
    if board[coords[1]][coords[0]] == "#":
        coords = (coords[0] + (direction[0] * -1), coords[1] + (direction[1] * -1))

        if direction == (0, -1):
            direction = (1, 0)

        elif direction == (1, 0):
            direction = (0, 1)

        elif direction == (0, 1):
            direction = (-1, 0)

        elif direction == (-1, 0):
            direction = (0, -1)

    else:
        visited.append(coords)
    
    coords = (coords[0] + direction[0], coords[1] + direction[1])

visited = set(visited[1:])

total = 0
for v in visited:
    board[v[1]][v[0]] = "#"

    if checkloop(start, (0, -1), board):
        total += 1

    board[v[1]][v[0]] = "."

print(total)