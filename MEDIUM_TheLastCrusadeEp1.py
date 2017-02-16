# w: number of columns.
# h: number of rows.
w, h = map(int, input().split())
lab = [tuple(map(int, input().split())) for i in range(h)]
ex = int(input())   # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

r, l, b = (1, 0), (-1, 0), (0, 1)
cells = (
    {},     # type 0
    {'TOP': b, 'LEFT': b, 'RIGHT': b},    # type 1
    {'LEFT': r, 'RIGHT': l}, {'TOP': b},  # type 2/3
    {'TOP': l, 'RIGHT': b}, {'TOP': r, 'LEFT': b},     # type 4/5
    {'LEFT': r, 'RIGHT': l}, {'TOP': b, 'RIGHT': b}, {'LEFT': b, 'RIGHT': b}, {'LEFT': b, 'TOP': b},     # type 6/7/8/9
    {'TOP': l}, {'TOP': r}, {'RIGHT': b}, {'LEFT': b},     # type 10/11/12/13
)

# game loop
while True:
    x, y, pos = input().split()
    x, y = int(x), int(y)
    move = cells[lab[y][x]][pos]
    print(x+move[0], y+move[1])
