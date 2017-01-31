import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the moutain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    # Find the highest mountain and destroy it
    highest_mountain = 0
    altitude_max = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > altitude_max:
            highest_mountain = i 
            altitude_max = mountain_h

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(highest_mountain)
