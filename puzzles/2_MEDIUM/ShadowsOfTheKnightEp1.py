# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over. Not used here.
x, y = [int(i) for i in input().split()]

inf_x, sup_x, inf_y, sup_y = 0, w-1, 0, h-1
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if bomb_dir[0] == 'U':
        sup_y = y - 1
    elif bomb_dir[0] == 'D':
        inf_y = y + 1
    if bomb_dir[-1] == 'L':
        sup_x = x - 1
    elif bomb_dir[-1] == 'R':
        inf_x = x + 1

    x = (sup_x + inf_x) // 2
    y = (sup_y + inf_y) // 2

    # the location of the next window Batman should jump to.
    print(str(x) + ' ' + str(y))
