import re
import string
ABC = string.ascii_lowercase


class Grid:
    width = 19
    height = 25
    symbol = "{}"

    def __init__(self):
        self.field = [[self.symbol] * self.width for _ in range(self.height)]

    def print_grid(self):
        for y in range(self.height):
            print("".join(x for x in self.field[y]))

    def crop(self, center: tuple[int, int], diameter: int):
        points_to_crop = self._get_points_in_circle(center=center, diameter=diameter)
        for point in points_to_crop:
            self.field[point[1]][point[0]] = "  "

    def plant(self, center: tuple[int, int], diameter: int):
        points_to_crop = self._get_points_in_circle(center=center, diameter=diameter)
        for point in points_to_crop:
            self.field[point[1]][point[0]] = self.symbol

    def plantmow(self, center: tuple[int, int], diameter: int):
        points_to_crop = self._get_points_in_circle(center=center, diameter=diameter)
        for point in points_to_crop:
            if self.field[point[1]][point[0]] == self.symbol:
                self.field[point[1]][point[0]] = "  "
            elif self.field[point[1]][point[0]] == "  ":
                self.field[point[1]][point[0]] = self.symbol

    @staticmethod
    def _get_points_in_circle(center: tuple[int, int], diameter: int) -> list[tuple[int, int]]:
        points = []
        for x in range(grid.width):
            for y in range(grid.height):
                if (x - center[0]) ** 2 + (y - center[1]) ** 2 < diameter ** 2 / 4:
                    points.append((x, y))
        return points


instructions = input().split()
grid = Grid()
regex = r"((?:PLANT|PLANTMOW)?)([a-z]{2})([0-9]{1,2})"
procedures = {
    "": grid.crop,
    "PLANT": grid.plant,
    "PLANTMOW": grid.plantmow
}
for instruction in map(re.compile(regex).match, instructions):
    apply_func = procedures[instruction.group(1)]
    center = (ABC.index(instruction.group(2)[0]), ABC.index(instruction.group(2)[1]))
    diameter = int(instruction.group(3))
    apply_func(center=center, diameter=diameter)

grid.print_grid()
