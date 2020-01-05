import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

opponent_count = int(input())  # Opponent count
targetX = random.randint(0, 34)
targetY = random.randint(0, 19)

# game loop
while 1:
    game_round = int(input())
    map = []
    opponents = []
    # x: Your x position
    # y: Your y position
    # back_in_time_left: Remaining back in time
    x, y, back_in_time_left = [int(i) for i in input().split()]

    for i in range(opponent_count):
        # opponent_x: X position of the opponent
        # opponent_y: Y position of the opponent
        # opponent_back_in_time_left: Remaining back in time of the opponent
        opponent_x, opponent_y, opponent_back_in_time_left = [int(j) for j in input().split()]
        opponents.append((opponent_x, opponent_y, opponent_back_in_time_left))

    for i in range(20):
        line = input()  # One line of the map ('.' = free, '0' = you, otherwise the id of the opponent)
        map.append(line)


    if (x != targetX or y != targetY) and map[targetY][targetX] == ".":
        pass
    else:
        targetX = random.randint(0, 34)
        targetY = random.randint(0, 19)

    print("%d %d" % (targetX, targetY))
