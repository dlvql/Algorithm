def solution(n, m):
    n, m = sorted([n, m])
    x, y = n, m
    while True:
        if x % y == 0:
            break
        x, y = y, x % y
    return [y, n * m / y]
        
        