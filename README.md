# Circle Game

## Overview

Circle Game is a simple interactive Python game in which the player must click on a moving circle twice to destroy it. The circle moves randomly around the screen, changing its position every 0.2 seconds. The game features a countdown timer before starting, and the objective is to click on the circle twice before it reaches the edges of the screen.

## Features

- **Graphical Interface**: Created using `graphics.py`, the game provides a visual window with interactive elements.
- **Interactive Gameplay**: Players must click on a moving circle to destroy it. If the circle reaches the edge of the screen, the game ends with a loss.
- **Countdown Timer**: The game begins with a 3-second countdown to prepare the player.

## Requirements

- Python 3.x
- `graphics.py` library (available [here](http://mcsp.wartburg.edu/zelle/python/graphics.py))
- `random`, `math`, `time` standard Python libraries

## How to Play

1. Clone or download this repository.
2. Install the required `graphics.py` library if you haven't already.
3. Run the script using Python:

    ```sh
    python circle_game.py
    ```

4. Read the instructions displayed in the game window.
5. Click on the circle twice to destroy it before it reaches the edge of the screen.
6. If you succeed, the game will display a win message. If you fail, you lose.

## Functions

### `distance(x1, y1, x2, y2)`
Calculates the distance between two points using the distance formula.

- **Inputs**: `x1`, `y1` (coordinates of the first point), `x2`, `y2` (coordinates of the second point)
- **Outputs**: `dist` (distance between the two points)

### `circle(x, y, color)`
Creates a circle object with a given position and color.

- **Inputs**: `x`, `y` (coordinates of the circle center), `color` (color of the circle)
- **Outputs**: `c` (circle object)

### `movement(x, y, window, color)`
Moves the circle to a new random position within a specified range.

- **Inputs**: `x`, `y` (coordinates of the current circle position), `window` (graphics window object), `color` (color of the circle)
- **Outputs**: `x`, `y` (new coordinates of the circle)

## Game Flow

1. **Introduction**: Displays the game instructions.
2. **Countdown**: Shows a 3-second countdown to prepare the player.
3. **Gameplay**: The circle moves randomly on the screen, and the player must click it twice.
4. **Win or Lose**:
   - If the player clicks the circle twice, they win.
   - If the circle hits the screen border, the player loses.

## Future Improvements

- **Improved Collision Detection**: Enhance the precision of detecting clicks on the circle.
- **Increased Difficulty Levels**: Add multiple levels with increasing difficulty, such as faster-moving circles.
- **Better Graphics**: Enhance visual elements to make the game more appealing.

## License

This project is open-source and available.

---

**Author**: Alexander Harshman
