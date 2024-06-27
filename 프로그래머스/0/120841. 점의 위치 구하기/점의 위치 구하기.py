def solution(dot):
    a, b = dot
    return 1 if a > 0 and b > 0 else 3 if a < 0 and b < 0 else 2 if a < 0 and b > 0 else 4