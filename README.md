# Battleships Game

This is a simple Battleships game implemented as a Flask web service. Players can start a new game, make guesses to locate ships.

## Features

- Start a new game.
- Make guesses to find the opponent's ships.
- Alternating turns between players after each guess.
- Visual feedback on the grid for hits ("X") and misses ("O").
- Check the game status, including grids and turn information.

## How to Play
- https://battleships-o91n.onrender.com

### Start a New Game

To start a new game, click at the "Start Game" button.

### Make a Guess

To make a guess, click at your choice on the grid, coordinates are (row and column).

### Game Status

"O" with blue background indicates a Miss and "X" with red background a Hit. 


### Installation

1. **Clone this repository:**
    ```bash
    git clone https://github.com/EdyDaSilva/battleships.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd battleships
    ```

3. **Create a virtual environment:**
    ```bash
    python -m venv myenv
    ```

4. **Activate the virtual environment:**
    - On Windows:
      ```bash
      myenv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source myenv/bin/activate
      ```

5. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Acknowledgments
Code Institute

