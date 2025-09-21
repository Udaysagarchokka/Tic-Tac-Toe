import tkinter as tk
from tkinter import messagebox
import json
import os

# --- File and Data Management ---

DATA_FILE = "bot_data.json"
initial_data = {
    "wins": 0,
    "losses": 0,
    "draws": 0
}


def load_data():
    """Loads game statistics and history from the data file."""
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        save_data(initial_data)
        return initial_data
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_data(data):
    """Saves game statistics to the data file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


# --- Minimax AI Logic ---

class TicTacToeAI:
    def __init__(self, player='X', opponent='O'):
        self.player = player
        self.opponent = opponent

    def find_best_move(self, board):
        """
        Finds the best move for the bot using the Minimax algorithm.
        """
        # The AI is the maximizing player
        best_score = -float('inf')
        best_move = None

        # Check all available moves
        for i in [i for i, spot in enumerate(board) if spot == '']:
            board[i] = self.player
            score = self.minimax(board, 0, False)
            board[i] = ''  # Undo the move

            if score > best_score:
                best_score = score
                best_move = i
        return best_move

    def minimax(self, board, depth, is_maximizing):
        """
        Recursive function to find the optimal move.
        """
        if self.check_winner(board, self.player):
            return 10 - depth
        if self.check_winner(board, self.opponent):
            return depth - 10
        if self.check_draw(board):
            return 0

        available_moves = [i for i, spot in enumerate(board) if spot == '']

        if is_maximizing:
            best_score = -float('inf')
            for i in available_moves:
                board[i] = self.player
                score = self.minimax(board, depth + 1, False)
                board[i] = ''
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in available_moves:
                board[i] = self.opponent
                score = self.minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(score, best_score)
            return best_score

    def check_winner(self, board, player):
        """Checks if the given player has won the game."""
        winning_combinations = [
            # Horizontal
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            # Vertical
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            # Diagonal
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if all(board[i] == player for i in combo):
                return True
        return False

    def check_draw(self, board):
        """Checks if the game is a draw."""
        return all(spot != '' for spot in board)


# --- GUI and Main Application ---

class TicTacToeApp:
    def __init__(self, master):
        self.master = master
        master.title("Unbeatable Gaming Bot")
        master.resizable(False, False)
        master.configure(bg='white')

        self.data = load_data()
        self.ai = TicTacToeAI()
        self.board = [''] * 9
        self.canvas = None
        self.is_game_over = False
        self.moves_made = []
        self.cell_size = 100
        self.message_window = None

        self.create_widgets()
        self.update_stats_display()

    def create_widgets(self):
        """Builds the main GUI elements."""

        # Main frames
        main_frame = tk.Frame(self.master, bg='white', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)

        # Left Panel for Statistics
        stats_frame = tk.Frame(main_frame, bg='white', bd=2, relief='solid', padx=10, pady=10)
        stats_frame.pack(side='left', fill='y', padx=(0, 20))

        tk.Label(stats_frame, text="Statistics", bg='white', font=("Arial", 14, "bold")).pack(pady=5)
        self.user_wins_label = tk.Label(stats_frame, text="User Wins: 0", bg='white', font=("Arial", 12))
        self.user_wins_label.pack(anchor='w')
        self.bot_wins_label = tk.Label(stats_frame, text="Bot Wins: 0", bg='white', font=("Arial", 12))
        self.bot_wins_label.pack(anchor='w')
        self.draws_label = tk.Label(stats_frame, text="Draws: 0", bg='white', font=("Arial", 12))
        self.draws_label.pack(anchor='w')

        # Reset Button
        reset_button = tk.Button(stats_frame, text="Reset Data", command=self.reset_data, font=("Arial", 10),
                                 bg="#f44336", fg="white", relief="raised")
        reset_button.pack(pady=10)

        # Game Board
        board_frame = tk.Frame(main_frame, bg='white')
        board_frame.pack(side='right')

        # Create canvas for the game board
        self.canvas = tk.Canvas(board_frame, width=3 * self.cell_size, height=3 * self.cell_size, bg='white',
                                highlightthickness=0)
        self.canvas.pack()
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.on_click)

        # Game Status Label
        self.status_label = tk.Label(self.master, text="Your Turn", font=("Arial", 16), bg='white')
        self.status_label.pack(pady=10)

    def draw_grid(self):
        """Draws the tic-tac-toe grid lines on the canvas."""
        self.canvas.create_line(self.cell_size, 0, self.cell_size, 3 * self.cell_size, fill='black', width=2)
        self.canvas.create_line(2 * self.cell_size, 0, 2 * self.cell_size, 3 * self.cell_size, fill='black', width=2)
        self.canvas.create_line(0, self.cell_size, 3 * self.cell_size, self.cell_size, fill='black', width=2)
        self.canvas.create_line(0, 2 * self.cell_size, 3 * self.cell_size, 2 * self.cell_size, fill='black', width=2)

    def draw_mark(self, index, mark):
        """Draws an 'X' or 'O' on the canvas at the specified index."""
        row, col = divmod(index, 3)
        x = col * self.cell_size + self.cell_size / 2
        y = row * self.cell_size + self.cell_size / 2
        self.canvas.create_text(x, y, text=mark, font=("Arial", 60, "bold"), fill='black')

    def update_stats_display(self):
        """Updates the labels with current win/loss/draw counts."""
        self.user_wins_label.config(text=f"User Wins: {self.data['losses']}")
        self.bot_wins_label.config(text=f"Bot Wins: {self.data['wins']}")
        self.draws_label.config(text=f"Draws: {self.data['draws']}")

    def show_custom_message(self, title, message, color):
        """Creates a custom, auto-closing message box."""
        self.message_window = tk.Toplevel(self.master)
        self.message_window.title(title)
        self.message_window.configure(bg=color)
        self.message_window.attributes('-topmost', True)  # Keep on top of other windows

        message_label = tk.Label(self.message_window, text=message, font=("Arial", 16), bg=color, fg="white", padx=20,
                                 pady=20)
        message_label.pack()

        # Schedule the window to close after 2 seconds
        self.master.after(2000, self.message_window.destroy)

    def on_click(self, event):
        """Handles a user's mouse click on the canvas."""
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        index = row * 3 + col

        if self.board[index] == '' and not self.is_game_over:
            self.board[index] = 'O'
            self.draw_mark(index, 'O')
            self.check_game_state()
            if not self.is_game_over:
                self.master.after(500, self.bot_move)

    def bot_move(self):
        """Handles the bot's turn."""
        if not self.is_game_over:
            self.status_label.config(text="Bot is thinking...", fg='red')

            bot_index = self.ai.find_best_move(self.board)

            if bot_index is not None:
                self.board[bot_index] = 'X'
                self.draw_mark(bot_index, 'X')

            self.check_game_state()
            if not self.is_game_over:
                self.status_label.config(text="Your Turn", fg='black')

    def check_game_state(self):
        """Checks for a win, loss, or draw and updates the UI."""
        if self.ai.check_winner(self.board, 'O'):
            self.is_game_over = True
            self.data['losses'] += 1
            self.status_label.config(text="You Win!", fg='green')
            self.show_custom_message("Game Over", "Congratulations, you won!", "green")

        elif self.ai.check_winner(self.board, 'X'):
            self.is_game_over = True
            self.data['wins'] += 1
            self.status_label.config(text="Bot Wins!", fg='red')
            self.show_custom_message("Game Over", "The bot won this time!", "red")

        elif self.ai.check_draw(self.board):
            self.is_game_over = True
            self.data['draws'] += 1
            self.status_label.config(text="It's a Draw!", fg='orange')
            self.show_custom_message("Game Over", "The game is a draw!", "orange")

        if self.is_game_over:
            self.update_stats_display()
            save_data(self.data)
            self.master.after(2000, self.reset_game)

    def reset_game(self):
        """Resets the game board for a new game."""
        self.board = [''] * 9
        self.canvas.delete("all")
        self.draw_grid()
        self.is_game_over = False
        self.status_label.config(text="Your Turn", fg='black')

    def reset_data(self):
        """Resets all game data and stats."""
        if messagebox.askyesno("Reset Data", "Are you sure you want to reset all game data?"):
            self.data = initial_data.copy()
            self.update_stats_display()
            save_data(self.data)
            self.reset_game()
            messagebox.showinfo("Data Reset", "All game data has been cleared.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
