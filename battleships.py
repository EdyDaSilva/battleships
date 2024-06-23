import random

def initialize_grid(size):
    return [["~" for _ in range(size)] for _ in range(size)]


def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


def place_ship(grid, size, ship_count):
    ships = []
    for _ in range(ship_count):
        while True:
            ship_row = random.randint(0, size-1)
            ship_col = random.randint(0, size-1)
            if (ship_row, ship_col) not in ships:
                ships.append((ship_row, ship_col))
                break
    return ships


def get_user_guess(size):
    while True:
        try:
            guess_row = int(input(f"Enter row (0-{size-1}): "))
            guess_col = int(input(f"Enter column (0-{size-1}): "))
            if 0 <= guess_row < size and 0 <= guess_col < size:
                return guess_row, guess_col
            else:
                print(f"Please enter numbers between 0 and {size-1}.")
        except ValueError:
            print("Please enter valid numbers.")

