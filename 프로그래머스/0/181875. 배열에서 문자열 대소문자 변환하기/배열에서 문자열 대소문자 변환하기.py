def solution(strArr):
    for i in range(len(strArr)):
        strArr[i] = strArr[i].upper() if i % 2 == 1 else strArr[i].lower()
    return strArr