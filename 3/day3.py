import math
from functools import reduce


def get_trees(down, right, grid):
    extended_grid = [
        row * (math.ceil(len(grid) / (len(grid[0]) / right))) for row in grid
    ]
    return len(
        [
            o
            for i, row in enumerate(extended_grid[down::down])
            if (o := row[(i + 1) * right] == "#")
        ]
    )


input = open("input.txt").read().split("\n")
part1 = get_trees(1, 3, input)
slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
part2 = reduce(lambda x, y: x * get_trees(y[0], y[1], input), slopes, 1)
print(part1)
print(part2)
