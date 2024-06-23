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


def check_guess(ships, guess_row, guess_col):
    if (guess_row, guess_col) in ships:
        print("Hit!")
        ships.remove((guess_row, guess_col))
        return True
    else:
        print("Miss!")
        return False
    

def update_grid(grid, guess_row, guess_col, hit):
    if hit:
        grid[guess_row][guess_col] = "X"
    else:
        grid[guess_row][guess_col] = "O"


def play_battleships():
    size = int(input("Enter grid size: "))
    ship_count = int(input("Enter number of ships: "))
    
    player1_grid = initialize_grid(size)
    player2_grid = initialize_grid(size)
    
    player1_ships = place_ship(player1_grid, size, ship_count)
    player2_ships = place_ship(player2_grid, size, ship_count)
    
    player1_turn = True
    
    while player1_ships and player2_ships:
        if player1_turn:
            print("Player 1's turn")
            print_grid(player2_grid)
            guess_row, guess_col = get_user_guess(size)
            hit = check_guess(player2_ships, guess_row, guess_col)
            update_grid(player2_grid, guess_row, guess_col, hit)
            if not hit:
                player1_turn = False
        else:
            print("Player 2's turn")
            print_grid(player1_grid)
            guess_row, guess_col = get_user_guess(size)
            hit = check_guess(player1_ships, guess_row, guess_col)
            update_grid(player1_grid, guess_row, guess_col, hit)
            if not hit:
                player1_turn = True
    
    if not player1_ships:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

if __name__ == "__main__":
    play_battleships()
