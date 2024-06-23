import os
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

def get_user_guess(size, player, turn):
    # Simulating guesses for demonstration
    guess_row = random.randint(0, size-1)
    guess_col = random.randint(0, size-1)
    print(f"Player {player}'s turn ({turn}). Guess: row {guess_row}, column {guess_col}")
    return guess_row, guess_col

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
    size = int(os.getenv("GRID_SIZE", 5))
    ship_count = int(os.getenv("SHIP_COUNT", 3))
    
    player1_grid = initialize_grid(size)
    player2_grid = initialize_grid(size)
    
    player1_ships = place_ship(player1_grid, size, ship_count)
    player2_ships = place_ship(player2_grid, size, ship_count)
    
    player1_turn = True
    turn = 1
    
    while player1_ships and player2_ships:
        if player1_turn:
            print("Player 1's turn")
            print_grid(player2_grid)
            guess_row, guess_col = get_user_guess(size, 1, turn)
            hit = check_guess(player2_ships, guess_row, guess_col)
            update_grid(player2_grid, guess_row, guess_col, hit)
            if not hit:
                player1_turn = False
        else:
            print("Player 2's turn")
            print_grid(player1_grid)
            guess_row, guess_col = get_user_guess(size, 2, turn)
            hit = check_guess(player1_ships, guess_row, guess_col)
            update_grid(player1_grid, guess_row, guess_col, hit)
            if not hit:
                player1_turn = True
        
        turn += 1
    
    if not player1_ships:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")

if __name__ == "__main__":
    play_battleships()
