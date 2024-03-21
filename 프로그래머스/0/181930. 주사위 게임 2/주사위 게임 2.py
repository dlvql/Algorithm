def solution(a, b, c):
    s = a + b + c
    if (a == b or b == c or a == c):
        s *= (a ** 2 + b ** 2 + c ** 2)
    if (a == b and b== c):
        s *= (a ** 3 + b ** 3 + c ** 3)
    return s