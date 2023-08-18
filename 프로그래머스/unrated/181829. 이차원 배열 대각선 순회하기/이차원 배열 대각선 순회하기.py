def solution(board, k):
    res = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i+j) <= k:
                res += board[i][j]
    return res