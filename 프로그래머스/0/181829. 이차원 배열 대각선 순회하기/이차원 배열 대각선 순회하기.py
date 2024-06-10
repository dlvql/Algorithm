def solution(board, k):
    s = 0
    for iIdx, i in enumerate(board):
        for jIdx, j in enumerate(i):
            if(iIdx + jIdx <= k):
                s += j
            
    return s