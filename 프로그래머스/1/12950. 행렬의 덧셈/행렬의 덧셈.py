def solution(arr1, arr2):
    ans = []
    for ar1, ar2 in zip(arr1, arr2):
        arr = []
        for i, j in zip(ar1, ar2):
            arr.append(i + j)
        ans.append(arr)
    return ans