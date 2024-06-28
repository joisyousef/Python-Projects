def player_wins(state, player):
    """
    Returns True if the given player ('X' or 'O') wins in
    the given state. Returns False otherwise.
    """
    player = player.upper()
    # Check rows
    for row in range(3):
        if (state[row][0] == state[row][1] 
                == state[row][2] == player):
            return True
    # Check columns
    for col in range(3):
        if (state[0][col] == state[1][col] 
                == state[2][col] == player):
            return True
    # Check diagonals
    if state[0][0] == state[1][1] == state[2][2] == player:
        return True
    if state[0][2] == state[1][1] == state[2][0] == player:
        return True
    # Player doesn't win
    return False

def nobody_wins(state):
    """
    Returns True if the given state is a tie.
    Otherwise, returns False.
    """
    # Check there are empty squares
    for row in range(3):
        for col in range(3):
            if state[row][col] == ' ':
                return False
    # Otherwise, check if somebody wins
    if player_wins(state, 'X'):
        return False
    if player_wins(state, 'O'):
        return False
    # Nobody wins
    return True
    
def terminal(state):
    """
    Returns True if the given state is terminal.
    Otherwise, returns False.
    """
    if player_wins(state, 'X'):
        return True
    if player_wins(state, 'O'):
        return True
    if nobody_wins(state):
        return True
    return False
    
def score(state):
    """
    Returns score (1: X wins, -1: O wins, zero: nobody wins)
    for terminal state only
    """
    if player_wins(state, 'X'):
        return 1
    if player_wins(state, 'O'):
        return -1
    if nobody_wins(state):
        return 0
            
def current_player(state):
    """
    Returns the current player ('X' or 'O') for the given state
    """
    # Count the number of Xs and Os
    count_X = 0
    count_O = 0
    for row in range(3):
        for col in range(3):
            symbol = state[row][col]
            if symbol == 'X':
                count_X += 1
            elif symbol == 'O':
                count_O += 1
    # If they are the same, it's player X's turn
    if count_X == count_O:
        return 'X'
    # Otherwise, it's player O's turn
    return 'O'
    
def available_actions(state):
    """
    Returns a list of all possible actions from the given state.
    Each action is a tuple of (player, row, col).
    Returns an empty list if no actions are available or if 
    the state is terminal.
    """
    # Check terminal state
    if terminal(state):
        return []
    # Get the current player
    player = current_player(state)
    # Determine all possible actions (for empty squares)
    actions = []
    for row in range(3):
        for col in range(3):
            if state[row][col] == ' ':
                actions.append((player, row, col))
    return actions
    
def next_state(state, action):
    """
    Applies the given action to the given state and 
    returns the new state
    """
    # copy state
    new_state = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    for row in range(3):
        for col in range(3):
            new_state[row][col] = state[row][col]
    # apply action to new_state
    (player, new_row, new_col) = action
    new_state[new_row][new_col] = player
    # return new_state
    return new_state

def initial_state():
    """
    Returns the initial state of the game (empty board)
    """
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

def display(state):
    """
    Prints the given state
    """
    print()
    for row in range(3):
        for col in range(3):
            print(' ', state[row][col], ' ', sep='', end='')
            if col < 2:
                print('|', end='')
        print()
        if row < 2:
            print('---+---+---', end='')
            print()
    print()

def human_action(state):
    """
    Waits for a human player to enter his action as input
    and returns this action.
    """
    player = current_player(state)
    invalid_action = True
    display_error = False
    while invalid_action:
        if display_error:
            print('Invalid action, please try again')
        display_error = True
        row, col = -1, -1
        row_col = input("Player {}'s turn: ".format(player))
        try:
            row, col = row_col.split()
            row, col = int(row), int(col)
        except:
            row, col = -1, -1
        if row < 0 or row > 2 or col < 0 or col > 2:
            invalid_action = True
            continue
        if state[row][col] != ' ':
            invalid_action = True
            continue
        invalid_action = False    
    return (player, row, col)
    
def ai_action(state, minimax):
    """
    Calculate and return the best move for AI player
    using the given minimax function to calculate
    the value of all possible next states and select
    the action the yields the best next state
    """
    player = current_player(state)
    print('AI player {} is thinking...'.format(player))
    # get all possible actions, next_states, and their values
    actions = available_actions(state)
    next_states = [next_state(state, a) for a in actions]
    values = [minimax(s) for s in next_states]
    # calculate the best value 
    if player == 'X':
        best_value = max(values)
    else:
        best_value = min(values)
    # return the action that yields the best value
    best_index = values.index(best_value)
    best_action = actions[best_index]
    (player, row, col) = best_action
    print('AI player {} chooses ({}, {})'.format(player, row, col))
    return best_action
    
def show_winner(state):
    """
    Display a message for the winner at the given state
    """
    final_score = score(state)
    if final_score == 1:
        print('Player X wins')
    elif final_score == -1:
        print('Player O wins')
    elif final_score == 0:
        print('Nobody wins')
    else:
        print("Game hasn't finished yet!")