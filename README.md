# Tic-Tac-Toe with MCTS

A simple implementation of Tic-Tac-Toe using Monte Carlo Tree Search (MCTS) for AI moves. Includes two AI strategies: epsilon-greedy and UCB-based.

## Files

### `MCTS.py`

Implements the MCTS algorithm for AI decision-making. Provides:
- `MCTS_epsilon_greedy`: Balances exploration/exploitation with an epsilon parameter.
- `MCTS_UCB`: Uses UCB1 for action selection, balancing exploration and exploitation.

### `TicTacToe.py`

Defines the Tic-Tac-Toe game logic:
- Board representation and state management.
- Move validation and state transitions.
- Win/loss/draw detection.

### `play.py`

Allows playing Tic-Tac-Toe against the AI:
- Choose 'X' or 'O' to play as.
- AI uses either `MCTS_epsilon_greedy` or `MCTS_UCB`.

## Parameters

Adjustable in `play.py`:
- `USE_UCB`: Toggle AI strategy (True for UCB, False for epsilon-greedy).
- `MAX_ITERS`: Number of MCTS iterations per move.
- `EPSILON`: Exploration rate for epsilon-greedy.
- `C`: UCB exploration-exploitation balance.
- `SEED`: Random seed for consistency.

## Example Gameplay
```
Welcome to Tic-Tac-Toe!
Do you want to play as 'X' or 'O'? (X goes first): X
You are playing as 'X'. You go first!
. . .
. . .
. . .
Your turn!
Enter your move (1-9): 1
X . .
. . .
. . .
AI is thinking...
AI chose position 5.
X . .
. O .
. . .
Your turn!
Enter your move (1-9): 2
X X .
. O .
. . .
AI is thinking...
AI chose position 3.
X X O
. O .
. . .
Your turn!
Enter your move (1-9): 4
X X O
X O .
. . .
AI is thinking...
AI chose position 7.
X X O
X O .
O . .
AI wins!
```