import numpy as np

def solution(board):
    board = np.array(board)
    size = len(board)
    area = len(board)**2
    bomb_rows, bomb_cols = np.where(board == 1)

    for row,col in zip(bomb_rows,bomb_cols):
        row_start, row_end = max(row-1,0),min(row+2,size)
        col_start, col_end = max(col-1,0),min(col+2,size)
        
        board[row_start:row_end,col_start:col_end] = 1        
        
    return area - int(np.sum(board))