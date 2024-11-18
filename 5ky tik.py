def is_solved(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    

    if any(0 in row for row in board):
        return -1
    

    return 0


board1 = [[0, 0, 1],
          [0, 1, 2],
          [2, 1, 0]]

board2 = [[1, 1, 1],
          [0, 2, 2],
          [0, 0, 0]]

print(is_solved(board1))  # -1
print(is_solved(board2))  # 1