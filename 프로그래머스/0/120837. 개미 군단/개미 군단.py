def solution(hp):
    a, c = [0, 0]
    for i in [5, 3, 1]:
        a = hp // i
        hp -= a * i
        c += a
    return c