# A couple constants
MOVES = {'S': (1, 0), 'E': (0, 1), 'N': (-1, 0), 'W': (0, -1)}
VERBOSE = {d[0]: d for d in 'SOUTH EAST NORTH WEST'.split()}

# Manage input
HEIGHT, WIDTH = map(int, input().split())
teleports = []
grid = []
for i in range(HEIGHT):
    line = list(input())
    if '@' in line:
        bender_y = i
        bender_x = line.index('@')
    while 'T' in line:  # Change 'T' with 't' to detect multiple teleports on the same line
        teleports.append((i, line.index('T')))
        line[teleports[-1][1]] = 't'
    grid += [line]

# Initialization
priorities = 'SENW'
breaker = False
direction = 'S'
visited = set()
log = []

# Game loop
while grid[bender_y][bender_x] != '$':

    # Move attempt
    previous = bender_y, bender_x
    bender_y += MOVES[direction][0]
    bender_x += MOVES[direction][1]

    # Obstacle management
    if breaker and grid[bender_y][bender_x] is 'X':
        grid[bender_y][bender_x] = ' '
    else:
        counter = 0
        while grid[bender_y][bender_x] in '#X':
            direction = priorities[counter]
            bender_y, bender_x = previous
            bender_y += MOVES[direction][0]
            bender_x += MOVES[direction][1]
            counter += 1

    # Logging
    log += [VERBOSE[direction]]

    # Modifier management
    modifier = grid[bender_y][bender_x]
    if modifier in 'SENW':
        direction = modifier
    if modifier is 'I':
        priorities = priorities[::-1]
    if modifier is 'B':
        breaker = not breaker
    if modifier is 't':
        bender_y, bender_x = (set(teleports) - {(bender_y, bender_x)}).pop()    # Use set difference

    # Loop detection
    status = bender_y, bender_x, tuple(tuple(line) for line in grid), direction, breaker
    if status in visited:
        log = ['LOOP']
        break
    else:
        visited.add(status)

# Output the log
print('\n'.join(log))
