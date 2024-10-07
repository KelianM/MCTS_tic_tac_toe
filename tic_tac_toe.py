import numpy as np

class TicTacToe:
    def __init__(self):
        # 1D array to represent the board, 0: empty, 1: X, 2: O
        self.board = np.zeros(9, dtype=int)
        self.current_player = 1  # 1 for X, 2 for O
        
    def reset(self):
        # Reset the board for a new game
        self.board.fill(0)
        self.current_player = 1
    
    def get_state(self):
        return self.board

    def set_state(self, board_list):
        self.board = np.array(board_list)

    def normalize_state(self):
        board_2d = self.board.reshape((3, 3))
        # Generate all transformations: rotations (0, 90, 180, 270) and reflections (vertical, horizontal)
        transformations = [
            board_2d,
            np.rot90(board_2d, 1),
            np.rot90(board_2d, 2),
            np.rot90(board_2d, 3),
            np.fliplr(board_2d),
            np.flipud(board_2d),
            np.rot90(np.fliplr(board_2d), 1),
            np.rot90(np.flipud(board_2d), 1)
        ]
        # Find the lexicographically smallest transformation as the normalized state
        min_state = min(transformations, key=lambda x: x.flatten().tolist())
        return min_state.flatten()
    
    def take_action(self, index):
        # Take an action and return new state, reward
        if self.board[index] != 0:
            raise ValueError("Invalid move")
        
        # Place current player's piece on the board
        self.board[index] = self.current_player
        
        # Check if the game is over
        is_over, reward = self.is_finished()
        
        # Switch to the other player
        self.current_player = 3 - self.current_player
        
        return self.board, reward
    
    def is_finished(self):
        # Define all possible winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        # Check for a win
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != 0:
                return True, 1 if self.board[combo[0]] == 1 else -1  # 1 if X wins, -1 if O wins
        
        # Check for a draw (no empty spaces left)
        if np.all(self.board != 0):
            return True, 0  # Draw
        
        # Game is still ongoing
        return False, 0
    
    def valid_moves(self):
        # Return the indices of empty spots (0)
        return [i for i in range(9) if self.board[i] == 0]

    def print_board(self):
        # Print the board in a readable format
        symbols = {0: '.', 1: 'X', 2: 'O'}
        print("\n".join(
            [" ".join([symbols[self.board[j]] for j in range(i, i + 3)]) for i in range(0, 9, 3)]
        ))