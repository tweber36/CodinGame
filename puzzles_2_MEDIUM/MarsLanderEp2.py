import math
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
coord_land = []
max_hspeed = 20
max_vspeed = 40
gravity = 3.711
speed_margin = 5
y_margin = 20

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point.
    # By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    coord_land.append((land_x, land_y))

print(coord_land, file=sys.stderr)


def find_landing_ground(land_points):
    i = 0
    while i < len(land_points) - 1:
        x1 = land_points[i][0]
        x2 = 0
        j = i+1
        while land_points[i][1] == land_points[j][1] and j < len(land_points):
            x2 = land_points[j][0]
            j += 1
        if (x2 - x1) >= 1000:
            return (x1, x2, land_points[i][1])
        i += 1
    return (-1, -1, -1)

(targetL, targetR, targetY) = find_landing_ground(coord_land) # (x1, x2) represents the landing zone
print(targetL, targetR, targetY, file=sys.stderr)


def angle_to_slow():
    speed = math.sqrt(v_speed**2 + h_speed**2)
    return int(math.degrees(math.asin(h_speed / speed)))


def angle_to_aim():
    angle = int(math.degrees(math.acos(gravity / 4.0)))
    if x < targetL:
        return -angle
    elif x > targetR:
        return angle
    else:
        return 0


def power_to_hover():
    if v_speed >= 0:
        return 3
    return 4

# game loop
while 1:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    if not (targetL <= x <= targetR):
        if (x < targetL and h_speed < 0) or (x > targetR and h_speed > 0) or (abs(h_speed) > 4 * max_hspeed):
            print(angle_to_slow(), "4")
        elif abs(h_speed) < 2 * max_hspeed:
            print(angle_to_aim(), "4")
        else:
            print("0", power_to_hover())
    else:
        if y < targetY + y_margin:
            print("0 3")
        elif (abs(h_speed) <= max_hspeed - speed_margin) and (abs(v_speed) <= max_vspeed - speed_margin):
            print("0 2")
        else:
            print(angle_to_slow(), "4")
