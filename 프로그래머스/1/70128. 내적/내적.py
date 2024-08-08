def solution(a, b):
    s = 0
    for (i, j) in zip(a, b):
        s += i * j
    return s