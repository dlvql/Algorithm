def solution(arr):
    idx1, idx2 = len(arr), -1 #1 = min & 2 = max
    for i in range(len(arr)):
        if(arr[i] == 2):
            idx1 = i if idx1 > i else idx1
            idx2 = i if idx2 < i else idx2
    return [-1] if idx1 == len(arr) and idx2 == -1 else arr[idx1:idx2+1]