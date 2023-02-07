# Snake Game
A classic snake game developed using the Pygame library. The game features a colourful interface and smooth gameplay. Includes source code and assets.

The game starts with a snake appearing in the middle of the screen. The user can control the snake using the arrow keys to move it around the screen. The objective of the game is to eat the food that randomly appears on the screen. Every time the snake eats the food, it grows in size, and the user's score increases.

The game ends when the snake collides with the wall or itself. 

The code is broken down into three classes: Food, Snake, and SnakeGame. The Food class holds information about the food's position and size. The Snake class holds information about the snake's head, body, and direction. The SnakeGame class is responsible for running the game and drawing the various elements on the screen. 

The game is run by calling the run function of the SnakeGame class. This function handles user input and updates the game accordingly. It also checks for collisions between the snake and the wall or itself. 

This game is a great way to pass some time and have some fun. Give it a try!

## Requirements

- Python 3.x
- Pygame library

## How to run the game

1. Make sure you have installed all the required libraries and dependencies.
2. Navigate to the directory where the game's files are located in the terminal or command prompt.
3. Run the main file for the game by using the command `python snake_game.py` or `python3 snake_game.py`.
4. The game should now start and you can play it.

## How to play the game

- Use arrow keys to control the movement of snake.
- Eat the food to grow the snake.
- Avoid hitting the walls or snake's own body.
- Game ends when snake hits the wall or its own body.
