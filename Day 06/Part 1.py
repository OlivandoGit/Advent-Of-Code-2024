board = []

with open("Input.txt") as file:
    board += [list(line.strip()) for line in file]


coords = (0, 0)

for y, line in enumerate(board):
    for x, char in enumerate(line):
        if char == "^":
            coords = (x, y)
            break
    else:
        continue

    break


direction = (0, -1)
total = 0

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
        board[coords[1]][coords[0]] = "X"
    
    coords = (coords[0] + direction[0], coords[1] + direction[1])


total = 0

for line in board:
    for char in line:
        if char == "X":
            total += 1

print(total)