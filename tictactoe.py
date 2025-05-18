"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    result = set()
    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                result.add((x,y))
    return result

def result(board, action):
    board = copy.deepcopy(board)
    if action not in actions(board):
        raise Exception("Illegal action!")
    p = player(board)
    board[action[0]][action[1]] = p
    return board


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None


def terminal(board):
    if winner(board) is not None:
        return True
    if len(actions(board)) != 0:
        return False
    else:
        return True

def utility(board):
    win = winner(board)
    if win is not None:
        return 1 if win == X else -1
    return 0


def minimax(board):
    if terminal(board):
        return None

    def max_value(state, current_val = math.inf):
        if terminal(state):
            return utility(state), None
        v = -math.inf
        best_action = None
        for action in actions(state):
            if v >= current_val:
                break
            min_v, _ = min_value(result(state, action), v)
            if min_v > v:
                v = min_v
                best_action = action
        return v, best_action

    def min_value(state, current_val = -math.inf):
        if terminal(state):
            return utility(state), None
        v = math.inf
        best_action = None
        for action in actions(state):
            if v <= current_val:
                break
            max_v, _ = max_value(result(state, action), v)
            if max_v < v:
                v = max_v
                best_action = action
        return v, best_action

    p = player(board)
    if p == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)
    return action