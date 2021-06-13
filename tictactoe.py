"""
Tic Tac Toe Player
"""

import math, copy

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
    x = 0
    o = 0
    empty = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == X:
                x += 1
            elif board[row][col] == O:
                o += 1
            else:
                empty += 1
    if empty == 0:
        return "the game is already over"
    elif x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibility = set()
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                possibility.add((row, col))
    return possibility


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new = copy.deepcopy(board)
    if action in actions(board):
        new[action[0]][action[1]] = player(board)
        return new
    else:
        raise Exception("Not valid")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] == X\
        or board[1][0] == board[1][1] == board[1][2] == X\
        or board[1][0] == board[1][1] == board[1][2] == X \
        or board[2][0] == board[2][1] == board[2][2] == X \
        or board[0][0] == board[1][0] == board[2][0] == X \
        or board[0][1] == board[1][1] == board[2][1] == X \
        or board[0][2] == board[1][2] == board[2][2] == X \
        or board[0][0] == board[1][1] == board[2][2] == X \
            or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][0] == board[0][1] == board[0][2] == O \
        or board[1][0] == board[1][1] == board[1][2] == O \
        or board[1][0] == board[1][1] == board[1][2] == O \
        or board[2][0] == board[2][1] == board[2][2] == O \
        or board[0][0] == board[1][0] == board[2][0] == O \
        or board[0][1] == board[1][1] == board[2][1] == O \
        or board[0][2] == board[1][2] == board[2][2] == O \
        or board[0][0] == board[1][1] == board[2][2] == O \
            or board[0][2] == board[1][1] == board[2][0] == O:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == O or winner(board) == X:
        return True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):  # bestMove
    """
    Returns the optimal action for the current player on the board.
    """
    # if empty, always return center as the best move
    if board == initial_state():
        return 1, 1
    # if game is over, return none
    if terminal(board):
        return None
    best_move = None
    if player(board) == X:
        min_val = -math.inf
        for action in actions(board):
            if min_val < min_value(result(board, action)):
                min_val = min_value(result(board, action))
                best_move = action
        return best_move
    else:
        max_val = math.inf
        for action in actions(board):
            if max_val > max_value(result(board, action)):
                max_val = max_value(result(board, action))
                best_move = action
        return best_move


def min_value(board) -> int:
    if terminal(board):
        return utility(board)
    curr_minimum = math.inf
    for action in actions(board):
        score = max_value(result(board, action))
        curr_minimum = min(curr_minimum, score)
    return curr_minimum


def max_value(board):
    if terminal(board):
        return utility(board)
    curr_maximum = -math.inf
    for action in actions(board):
        score = min_value(result(board, action))
        curr_maximum = max(curr_maximum, score)
    return curr_maximum
