def solution(s):
    isDigit = True
    if (len(s) != 4) and (len(s) != 6):
        isDigit = False
    else:
        for i in s:
            if not i.isdigit():
                isDigit = False
                break
    return isDigit