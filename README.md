# Tic-Tac-Toe
A Self-Learning Game based on Min-Max Algorithm Designed for Study Purpose

Project Summary
The core of this project is a Tic-Tac-Toe game where a bot learns to play using the minimax algorithm. This algorithm is a decision-making strategy often used in artificial intelligence for games. It works by exploring all possible moves from the current state and assigning a score to each move based on whether it leads to a win, loss, or draw.

Objective: To create a Tic-Tac-Toe game where the bot learns to make optimal moves.

Key Algorithm: The minimax algorithm is used to determine the best possible move for the bot. It's a recursive algorithm that evaluates the game tree.

Learning Mechanism: The bot's "learning" is based on the minimax algorithm's ability to analyze all potential future moves and their outcomes. It doesn't truly "learn" from past mistakes in the way a neural network might; instead, it's pre-programmed with a perfect strategy that it can apply perfectly.

Data Storage: The bot_data.json file is likely used to store pre-calculated game states or to save the state of the bot's "knowledge" between sessions, perhaps to make it more efficient on subsequent runs.

Minimax Algorithm Explained
The minimax algorithm is a perfect strategy for two-player games with perfect information, like Tic-Tac-Toe. The "min" and "max" in its name refer to the two players:

Maximizer: This is the AI bot. Its goal is to maximize its score, which means finding a path to victory. A win for the maximizer is a positive score (e.g., +10).

Minimizer: This is the human opponent. Their goal is to minimize the maximizer's score, which means finding a path to victory for themselves. A win for the minimizer is a negative score (e.g., -10).

The algorithm works by recursively exploring the game tree. It assumes the opponent will always make the best possible move for them (the one that minimizes the bot's score).

The algorithm proceeds as follows:

Evaluate the Board: Assign a score to each possible outcome. A bot win gets a high score, a human win gets a low score, and a draw gets a neutral score.

Recursion: The algorithm explores all possible moves from the current state.

Backpropagation: Scores are passed back up the game tree.

On a maximizer's turn, it chooses the move that leads to the maximum possible score from the options available.

On a minimizer's turn, it chooses the move that leads to the minimum possible score from the options available.

Best Move Selection: The bot ultimately chooses the move that leads to the highest possible final score, assuming the opponent plays perfectly to counter it.

Project Setup Instructions
Based on your description, here are the steps to get the project running:

Create a Folder: Create a new, empty folder, for example, Gaming_bot.

Place the Code: Put the Tic-Tac-Toe Python code file inside this folder.

Create a Virtual Environment: It is good practice to create a virtual environment to manage project dependencies.

Open a terminal or command prompt and navigate to your Gaming_bot folder.

Run python -m venv venv to create a virtual environment named venv.

Activate the Virtual Environment:

On Windows: venv\Scripts\activate

On macOS/Linux: source venv/bin/activate

Install Dependencies: Install any required libraries (e.g., pip install some_library).

Run the File: Execute the Python file.

Check for bot_data.json: After the first run, the bot_data.json file should be created in the Gaming_bot folder. If it's not, you may need to create it manually as an empty JSON file ({}).

This project is an excellent way to learn about game theory, AI algorithms, and recursive programming. It's a classic example of how a simple algorithm can be used to create an unbeatable opponent in a deterministic game.
