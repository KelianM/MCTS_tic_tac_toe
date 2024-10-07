import numpy as np
import random
from tic_tac_toe import TicTacToe

model = TicTacToe()

class Node:
    def __init__(self, state, action=None, parent=None):
        self.state = state  # The state of the game at this node
        self.parent = parent  # Reference to the parent node
        self.action = action  # RAction taken to reach the node
        self.children = []  # List of child nodes
        self.visits = 0  # Number of times this node has been visited
        self.value = 0  # Estimated value of this node
        model.set_state(state)
        self.untried_actions = model.valid_moves()  # List of actions that have not been tried yet from this state

    def add_child(self, child_node):
        self.children.append(child_node)

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0
    
    def is_terminal(self):
        model.set_state(self.state)
        model.is_finished()

def MCTS(start_state, player, epsilon = 0.1, max_iters=100):
    root = Node(state=start_state)
    for i in range(max_iters):
        ######## Select ########
        node = root
        while node.is_fully_expanded() and not node.is_terminal():
            if np.random.rand() < epsilon:
                # Exploration: choose a random child
                node = random.choice(node.children)
            else:
                # Exploitation: choose child with highest value
                node = max(node.children, key=lambda x: x.value)
        if not node.is_fully_expanded():
            ######## Expand ########
            action = random.choice(node.untried_actions)
            model.set_state(node.state)
            state, reward = model.take_action(action)
            if not model.is_finished():
                state, reward = model.take_action(random.choice(model.valid_moves())) # random reply by opponent
            child_node = Node(state=state, parent=node, action=action)
            node.add_child(child_node)

            ######## Simulate ########
            simulate_state = child_node.state
            model.set_state(simulate_state)  # Set simulation state
            while not model.is_finished():
                # Random rollout
                state, reward = model.take_action(random.choice(model.valid_moves()))
            
            # Terminal reward for player (inverted when playing player 2 (O))
            reward = reward if player == 1 else reward * -1
            ######## Backup ########
            # Backpropagate the reward from the expanded node
            current_node = child_node
            while current_node is not None:
                current_node.value += reward
                current_node = current_node.parent
    # Return greedy selection
    greedy_node = max(root.children, key=lambda x: x.value)
    return greedy_node.action
    