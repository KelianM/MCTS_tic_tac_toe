import numpy as np
import random
from tic_tac_toe import TicTacToe
from MCTS import MCTS

MAX_ITERS = 100  # Constant for the number of MCTS iterations

def play_tic_tac_toe():
    # Initialize the game and variables
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe!")
    
    # Select player
    player_symbol = input("Do you want to play as 'X' or 'O'? (X goes first): ").upper()
    while player_symbol not in ['X', 'O']:
        player_symbol = input("Invalid choice. Please select 'X' or 'O': ").upper()
    
    user_player = 1 if player_symbol == 'X' else 2  # 1 for X, 2 for O
    ai_player = 3 - user_player  # Opposite player (2 for O, 1 for X)
    
    print(f"You are playing as '{player_symbol}'. {'You go first!' if user_player == 1 else 'AI goes first!'}")
    game.print_board()
    
    # Determine who goes first
    user_turn = user_player == 1
    
    # Play until the game ends
    while not game.is_finished()[0]:
        if user_turn:
            # User's turn
            print("Your turn!")
            valid = False
            while not valid:
                try:
                    user_move = int(input("Enter your move (1-9): ")) - 1
                    if user_move in game.valid_moves():
                        game.take_action(user_move)
                        valid = True
                    else:
                        print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter a number between 1 and 9.")
        else:
            # AI's turn
            print("AI is thinking...")
            state = game.get_state().tolist()
            ai_move = MCTS(state, player=ai_player, max_iters=MAX_ITERS)
            game.take_action(ai_move)
            print(f"AI chose position {ai_move + 1}.")
        
        # Print the board after each move
        game.print_board()
        
        # Check if the game has ended
        game_over, reward = game.is_finished()
        if game_over:
            if reward == 1:
                print("X wins!" if user_player == 1 else "AI wins!")
            elif reward == -1:
                print("O wins!" if user_player == 2 else "AI wins!")
            else:
                print("It's a draw!")
            break
        
        # Switch turns
        user_turn = not user_turn

if __name__ == "__main__":
    play_tic_tac_toe()