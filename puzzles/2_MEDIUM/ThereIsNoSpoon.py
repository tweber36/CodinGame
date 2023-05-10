# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

grid = [input() for _ in range(height)]

def find_right_node(grid, x, y):
    for i in range(x + 1, width):
        if grid[y][i] == '0':
            return i, y
    return -1, -1    
    
def find_bottom_node(grid, i, j):
    for i in range(y + 1, height):
        if grid[i][x] == '0':
            return x, i
    return -1, -1

for y in range(height):
    for x in range(width):
        if grid[y][x] == '0':
            rx, ry = find_right_node(grid, x, y)
            bx, by = find_bottom_node(grid, x, y)
            print("%d %d %d %d %d %d" % (x, y, rx, ry, bx, by))
