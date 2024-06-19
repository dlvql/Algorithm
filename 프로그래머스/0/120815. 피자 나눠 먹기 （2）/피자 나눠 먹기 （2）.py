def solution(n):
    x, y, z = [n, 6, -1]
    while True:
        z = x % y
        if z == 0:
            break
        x, y = y, z
    return n // y