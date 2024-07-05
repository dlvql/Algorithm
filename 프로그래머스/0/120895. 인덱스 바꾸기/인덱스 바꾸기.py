def solution(s, num1, num2):
    s = list(s)
    s[num1], s[num2] = s[num2], s[num1]
    return "".join(s)