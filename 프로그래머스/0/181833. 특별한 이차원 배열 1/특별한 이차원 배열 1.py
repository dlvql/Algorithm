def solution(n):
    ans = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(int(i == j))
        ans.append(arr)
    return ans