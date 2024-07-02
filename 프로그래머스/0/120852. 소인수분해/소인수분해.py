def solution(n):
    arr = set(list(range(2, n + 1)))
    ans = set()
    for i in range(2, n + 1):
        if i in arr:
            for j in range(i, n + 1, i):
                arr.discard(j)
            arr.add(i)
    for i in arr:
        if n % i == 0:
            ans.add(i)
    return list(sorted(ans))
        