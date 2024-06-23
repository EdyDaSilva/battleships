import random

def initialize_grid(size):
    return [["~" for _ in range(size)] for _ in range(size)]


def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

