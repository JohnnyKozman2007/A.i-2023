"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None
import random

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
    x_count = 0
    o_count = 0
    for l in board:
        for x in l:
            if x == "X":
                x_count += 1
            elif x == "O":
                o_count += 1 
    if x_count > o_count:
        return O
    else:
        return X
                

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_of_actions = set()
    for l in range(len(board)):
        for x in range(len(board[l])):
            if board[l][x] == EMPTY:
                set_of_actions.add((l,x))
    return set_of_actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError('Invalid move')
    else:
        mod_board = copy.deepcopy(board)
        mod_board[action[0]][action[1]] = player(board)
        return mod_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] == X or board[i][0] == O:
                return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            if board[0][i] == X or board[0][i] == O:
                return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[1][1] == X or board[1][1] == O:
            return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[1][1] == X or board[1][1] == O:
            return board[0][2]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif EMPTY in [x for i in board for x in i]:
        return False
    else:
        return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        state = winner(board)
        if state == X:
            return 1
        elif state == O:
            return -1
        else:
            return 0
    raise NotImplementedError

def minimax(board):
    if player(board) == O:
        util = -1
        state = False
    else:
        util = 1

    non_empty = 0
    for E in [x for i in board for x in i]:
        if E == EMPTY:
            non_empty += 1
    if non_empty >= 8:
        return random.sample(actions(board),1)[0]
    def minimax2(board,state = True):
        """
        Returns the optimal action for the current player on the board.
        """
        if state:
            v = float('-inf')
            best_move = None
            if terminal(board):
                return [utility(board)*util]
            for action in actions(board):
                v = max(v,minimax2(result(board,action),False)[0])
                if v == minimax2(result(board,action),False)[0]:
                    best_move = action
                    if terminal(board):

                        if utility(result(board,best_move)) == 1:
                            print(result(board,best_move))
            #print(result(board,best_move))
            return v,best_move
        else:
            v = float('inf')
            best_move = None
            if terminal(board):
                return [utility(board)*util]
            for action in actions(board):
                v = min(v,minimax2(result(board,action),True)[0])
                if v == minimax2(result(board,action),True)[0]:
                    best_move = action
            #print(result(board,best_move))
            return v,best_move
    #print(board)
    best = minimax2(board)
    #print(best)
    return best[1]