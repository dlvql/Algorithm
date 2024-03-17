def solution(arr, idx):
    ans = -1
    for i in range(idx, len(arr)):
        if(arr[i] == 1):
            ans = i
            break
    return ans