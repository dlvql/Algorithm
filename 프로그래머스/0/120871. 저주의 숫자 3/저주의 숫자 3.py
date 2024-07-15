def solution(n):
    c = 0
    i = 0
    while c < n:
        c += 1
        i += 1
        while '3' in list(str(i)) or i % 3 == 0:
            i += 1
    return i