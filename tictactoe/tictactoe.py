"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if(board == initial_state()):
        return X
    countX = 0
    countO = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                countX = countX + 1
            elif (board[i][j] == O):
                countO = countO + 1
    return (O, X)[countX == countO]

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    try:
        if(player(board) == X):
            new_board[action[0]][action[1]] = X
        else:
            new_board[action[0]][action[1]] = O
    except:
        print("Action is invalid")
        raise

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(board[0][0] == board[0][1] == board[0][2] or board[0][0] == board[1][0] == board[2][0] or board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    elif(board[0][2] == board[1][2] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        return board[0][2]
    elif(board[2][0] == board[2][1] == board[2][2] or board[0][1] == board[1][1] == board[2][1]):
        return board[2][1]
    elif(board[1][0] == board[1][1] == board[1][2]):
        return board[1][0]
    else:
        return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return (winner(board) == X or winner(board) == O or len(actions(board)) == 0)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == X):
        return 1
    elif(winner(board) == O):
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == terminal(board):
        return None
    if board == initial_state():
        return (1, 1)
    if player(board) == X:
        value = float('-inf')
        move = ()
        for action in actions(board):
            #print(str(action[0])+", "+str(action[1]))
            minval = minvalue(result(board, action))
            #print("v value "+str(v))
            if minval > value:
                value = minval
                move = action
        #print("Move: "+str(move[0])+", "+str(move[1]))
        return move
   
    if player(board) == O:
        value = float('inf')
        move = ()
        for action in actions(board):
            #print(str(action[0])+", "+str(action[1]))
            maxval = maxvalue(result(board, action))
            #print("v value "+str(v))
            if(maxval < value):
                value = maxval
                move = action
        #print(str(move[0])+", "+str(move[1]))
        return move

def maxvalue(board):
    if terminal(board):
        return utility(board)
    value = float('-inf')
    for action in actions(board):
        value = max(value, minvalue(result(board, action)))
    return value

def minvalue(board):
    if terminal(board):
        return utility(board)
    value = float('inf')
    for action in actions(board):
        value = min(value, maxvalue(result(board, action)))
    return value