# -*- coding: utf-8 -*-
"""code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l0iCAmNFiRxWzXE_MIKwq1IuVqJGszTU
"""

def makeCompMove(self):
  row, col = -1, -1
  while not self.makeMove(row, col, 'O'):
      col = random.randint(1,boardSize)
      row = random.randint(1,boardSize)
  print("Computer chose: "+str(row)+","+str(col))
  minimax(0, 0, True, self.marks, self.MIN, self.MAX)

def minimax(self, depth, nodeIndex, maximizingPlayer, values, alpha, beta):  
  if depth == self.boardSize:  
      return values[nodeIndex]
  if maximizingPlayer:  
      best = self.MIN  
      for i in range(0, 2):  
          val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)  
          best = max(best, val)  
          alpha = max(alpha, best)  
          if beta <= alpha:  
              break 
      return best  
      
  else: 
      best = self.MAX 
      for i in range(0, 2):  
          val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)  
          best = min(best, val)  
          beta = min(beta, best)  
          if beta <= alpha:  
              break 
      return best

board = [
    [ 'x', 'o', 'x' ],
    [ 'o', 'o', 'x' ],
    [ '_', '_', '_' ]
]
 
bestMove = minimax(board)

Max, Min = 'x', 'o'
def Moves_left(board) :
 
    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == '_') :
                return True
    return False

def evaluate(b):
#Row_wise
    for row in range(3) :    
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :       
            if (b[row][0] == Max) :
                return Max
            elif (b[row][0] == Min) :
                return Min
#column_wise
    for col in range(3) :
      
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
         
            if (b[0][col] == Max) :
                return Max
            elif (b[0][col] == Min) :
               return Min
#right_diagonal
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
     
        if (b[0][0] == Max) :
            return Max
        elif (b[0][0] == Min) :
            return Min
#left_diagonal
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
     
        if (b[0][2] == Max) :
            return Max
        elif (b[0][2] == Min) :
            return Min
    return 0

def minimax(board, depth, isMax) :
    value = evaluate(board)

    if (value == 10) :
        return value

    if (value == -10) :
        return value

    if (Moves_left(board) == False) :
        return 0
    if (isMax) :    
        best = -1000
        dx, dy = None, None 

        for i in range(3) :        
            for j in range(3) :

                if (board[i][j]=='_') :
                    board[i][j] = Max
                    sc = minimax(board,depth + 1,not isMax)
                    if best < sc:
                      dx, dy = i, j  
                      best = sc 
                    board[i][j] = '_'
        return best, dx, dy 
    else :
      best = 1000
      for i in range(3) :        
          for j in range(3) :
              if (board[i][j] == '_') :
                  board[i][j] = Min
                  pc = minimax(board, depth + 1, not isMax)
                  if best>pc:
                    xx,xy= i,j
                    best = pc
                    board[i][j]= '_'
      return best,xx,xy;
 
    board = [
    [ 'x','_'  '_' ],
    [ '_', 'o', 'x' ],
    [ 'o', '_', '_' ]
]
print(minimax(board,0,True))

import copy
import math
import random


X = "X"
O = "O"
EMPTY = None
user = None
ai = None


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
    count = 0
    for i in board:
        for j in i:
            if j:
                count += 1
    if count % 2 != 0:
        return ai
    return user


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    board_len = len(board)
    for i in range(board_len):
        for j in range(board_len):
            if board[i][j] == EMPTY:
                res.add((i, j))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curr_player = player(board)
    result_board = copy.deepcopy(board)
    (i, j) = action
    result_board[i][j] = curr_player
    return result_board


def get_horizontal_winner(board):
    # check horizontally
    winner_val = None
    board_len = len(board)
    for i in range(board_len):
        winner_val = board[i][0]
        for j in range(board_len):
            if board[i][j] != winner_val:
                winner_val = None
        if winner_val:
            return winner_val
    return winner_val


def get_vertical_winner(board):
    # check vertically
    winner_val = None
    board_len = len(board)
    for i in range(board_len):
        winner_val = board[0][i]
        for j in range(board_len):
            if board[j][i] != winner_val:
                winner_val = None
        if winner_val:
            return winner_val
    return winner_val


def get_diagonal_winner(board):
    # check diagonally
    winner_val = None
    board_len = len(board)
    winner_val = board[0][0]
    for i in range(board_len):
        if board[i][i] != winner_val:
            winner_val = None
    if winner_val:
        return winner_val

    winner_val = board[0][board_len - 1]
    for i in range(board_len):
        j = board_len - 1 - i
        if board[i][j] != winner_val:
            winner_val = None

    return winner_val


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner_val = get_horizontal_winner(board) or get_vertical_winner(board) or get_diagonal_winner(board) or None
    return winner_val


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_val = winner(board)
    if winner_val == X:
        return 1
    elif winner_val == O:
        return -1
    return 0


def maxValue(state):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v, minValue(result(state, action)))
    return v


def minValue(state):
    if terminal(state):
        return utility(state)
    v = math.inf
    for action in actions(state):
        v = min(v, maxValue(result(state, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)

    if current_player == X:
        min = -math.inf
        for action in actions(board):
            check = minValue(result(board, action))  # FIXED
            if check > min:
                min = check
                move = action
    else:
        max = math.inf
        for action in actions(board):
            check = maxValue(result(board, action))  # FIXED
            if check < max:
                max = check
                move = action
    return move


if __name__ == "__main__":
    board = initial_state()
    ai_turn = False
    print("Choose a player")
    user=input()
    if user == "X":
        ai = "O"
    else:
        ai = "X"
    while True:
        game_over =terminal(board)
        playr = player(board)
        if game_over:
            winner = winner(board)
            if winner is None:
                print("Game Over: Tie.")
            else:
                print(f"Game Over: {winner} wins.")
            break;
    
        else:
            if user != playr and not game_over:
                 if ai_turn:
                        move = minimax(board)
                        board = result(board, move)
                        ai_turn = False
                        print(board)

            elif user == playr and not game_over:
                ai_turn = True
                print("Enter the position to move (row,col)")
                i=int(input("Row:"))
                j=int(input("Col:"))
                if board[i][j] == EMPTY:
                    board = result(board, (i, j))
                    print(board)