def solution(arr):
    s = 1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[i][j] != arr[j][i]):
                s = 0
                break
    return s