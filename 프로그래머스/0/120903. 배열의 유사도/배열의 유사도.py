def solution(s1, s2):
    c = 0
    for i in s1:
        c += 1 if i in s2 else 0
    return c