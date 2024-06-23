# Battleships Game

This is a simple command-line based Battleships game written in Python. Two players take turns to guess the location of each other's ships on a grid. The game continues until one player has successfully hit all of the opponent's ships.

## Features

- Players can set the grid size.
- Players can set the number of ships.
- The game warns the user if their guess is off-grid.
- Hits and misses are displayed on the grid.
- The game tracks and displays the number of attempts.

## How to Play

1. **Setup**: Each player will have their own grid. Ships are placed randomly on the grid.
2. **Turns**: Players take turns to guess the location of the opponent's ships by entering the row and column numbers.
3. **Hits and Misses**: The grid updates with 'X' for hits and 'O' for misses.
4. **Winning**: The game ends when one player has no ships left.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/EdyDaSilva/battleships.git
    ```

2. Navigate to the project directory:
    ```bash
    cd battleships
    ```

3. Create a virtual environment:
    ```bash
    python -m venv myenv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```bash
      myenv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source myenv/bin/activate
      ```

5. Install required packages (if any):
    ```bash
    pip install -r requirements.txt
    ```

### Running the Game

Run the game script:
```bash
python battleships.py

