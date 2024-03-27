## alpha-beta剪枝搜索
##  杀棋检验
##  哈希优化
## 我们定义棋盘上-1为默认值，1为黑棋，0为白棋
## 进攻防守需要分开讨论
import random
import numpy as np

BOARD_SIZE = 15
## 剪枝搜索
def ai_move(board):
    best_score = float('inf')
    best_move = None
    for i in range(BOARD_SIZE+1):
        for j in range(BOARD_SIZE+1):
            if board[i, j] == -1:
                board[i, j] = 0
                score = alphabeta(board, 4, float('-inf'), float('inf'), False)
                board[i, j] = -1
                if score < best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def is_game_over(board):
    # 直接暴力，需要优化的话我们就仅仅针对当前落子位置给一个检查就行
    for i in range(BOARD_SIZE+1):
        for j in range(BOARD_SIZE+1-4):
            arr_row=board[i,j:j+5]
            arr_col=board[j:j+5,i]
            if np.all(arr_row == 1) or np.all(arr_row==0) or np.all(arr_col==1) or np.all(arr_col==1):
                return True
    arr=np.zeros(5)
    for i in range(BOARD_SIZE+1-4):
        for j in range(BOARD_SIZE+1-4):
            for k in range(5):
                arr[k]=board[i+k,j+k]
            if np.all(arr==1) or np.all(arr==0) :
                return True
    for i in range(4,BOARD_SIZE+1):
        for j in range(BOARD_SIZE+1-4):
            for k in range(5):
                arr[k]=board[i-k,j+k]
            if np.all(arr==1) or np.all(arr==0):
                return True
    return False

def evaluate(Board):
    # 在实际的五子棋AI中，可以使用更复杂的评估函数来评估当前局面的得分，
    # 我们需要同时考虑进攻与防御

    return 0


def alphabeta(board, depth, alpha, beta, player):
    if depth == 0 or is_game_over(board):
        return evaluate(board)

    if player:
        max_eval = float('-inf')
        for i in range(BOARD_SIZE+1):
            for j in range(BOARD_SIZE+1):
                if board[i, j] == -1:
                    board[i, j] = 0
                    eval = alphabeta(board, depth - 1, alpha, beta, False)
                    board[i, j] = -1
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i, j] == -1:
                    board[i, j] = 1
                    eval = alphabeta(board, depth - 1, alpha, beta, True)
                    board[i, j] = -1
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

## 判断当前状态是否成杀
def is_win():

    return