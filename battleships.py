from flask import Flask, request, jsonify, send_from_directory
import os
import random

app = Flask(__name__)

games = {}

def initialize_grid(size):
    return [["~" for _ in range(size)] for _ in range(size)]

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

def check_guess(ships, guess_row, guess_col):
    if (guess_row, guess_col) in ships:
        ships.remove((guess_row, guess_col))
        return "Hit!"
    else:
        return "Miss!"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.json
    size = data.get('size', 5)
    ship_count = data.get('ship_count', 3)
    game_id = str(len(games) + 1)
    
    player1_grid = initialize_grid(size)
    player2_grid = initialize_grid(size)
    player1_ships = place_ship(player1_grid, size, ship_count)
    player2_ships = place_ship(player2_grid, size, ship_count)
    
    games[game_id] = {
        'size': size,
        'ship_count': ship_count,
        'player1': {'grid': player1_grid, 'ships': player1_ships},
        'player2': {'grid': player2_grid, 'ships': player2_ships},
        'turn': 1
    }
    
    return jsonify({'game_id': game_id, 'message': 'Game started'}), 200

@app.route('/guess', methods=['POST'])
def make_guess():
    data = request.json
    game_id = data['game_id']
    player = data['player']
    guess_row = data['row']
    guess_col = data['col']
    
    game = games.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    
    opponent = 'player2' if player == 1 else 'player1'
    ships = game[opponent]['ships']
    
    result = check_guess(ships, guess_row, guess_col)
    if result == "Hit!":
        game[opponent]['grid'][guess_row][guess_col] = "X"
    else:
        game[opponent]['grid'][guess_row][guess_col] = "O"
    
    game['turn'] += 1
    if not ships:
        return jsonify({'game_id': game_id, 'result': f'Player {player} wins!', 'grid': game[opponent]['grid']}), 200
    
    return jsonify({'game_id': game_id, 'result': result, 'turn': game['turn'], 'grid': game[opponent]['grid']}), 200

@app.route('/game_status/<game_id>', methods=['GET'])
def game_status(game_id):
    game = games.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    
    return jsonify(game), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
