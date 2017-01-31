import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

# game loop
while True:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    # Before the jump, speed must be at value gap + 1 to cross the gap
    # If it's above it should slow down unless there's no time before the jump
    if coord_x < road:
        if speed < gap + 1:
            print("SPEED")
        elif speed > gap + 1 and coord_x + speed - 1 < road:
            print("SLOW")
        elif coord_x + speed >= road:
            print("JUMP")
        else:
            print("WAIT")

    # After the jump, slow down as fast as possible
    if coord_x + 1 >= road + gap:
        print("SLOW")
    


