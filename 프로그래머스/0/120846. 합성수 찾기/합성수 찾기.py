def solution(n):
    arr = set(range(1, n + 1))
    for i in range(2, n + 1):
        if(i in arr):
            for j in range(i, n + 1, i):
                arr.discard(j)
            arr.add(i)
    return n - len(arr)