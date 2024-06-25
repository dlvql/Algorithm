def solution(n):
    c = 0
    for i in range(1, n + 1):
        if ((n // i) * i) == n:
            c += 1
    return c