def solution(a, b):
    i = b
    while b != 0:
        a, b = b, a % b
    i /= a
    while i >= 2 and i % 2 == 0:
        i /= 2
    while i >= 5 and i % 5 == 0:
        i /= 5
    if i != 1:
        return 2
    else:
        return 1
    