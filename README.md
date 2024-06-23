# Battleships Game

This is a simple Battleships game implemented as a Flask web service. Players can start a new game, make guesses to locate ships, and check the game status through HTTP endpoints.

## Features

- Start a new game with a configurable grid size and number of ships.
- Make guesses to find the opponent's ships.
- Check the game status, including grids and turn information.

## How to Play

### Start a New Game

To start a new game, make a `POST` request to the `/start_game` endpoint with the desired grid size and number of ships.

### Make a Guess

To make a guess, make a `POST` request to the `/guess` endpoint with the game ID, player number, and guess coordinates (row and column).

### Check Game Status

To check the game status, make a `GET` request to the `/game_status/<game_id>` endpoint.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Flask installed (can be added via `requirements.txt`).

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

### Running the Game Locally

To run the Flask application locally:

```bash
python battleships.py
