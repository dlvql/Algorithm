def solution(myString, pat):
    l = len(pat)
    c = 0
    for i in range(len(myString) - l + 1):
        if(myString[i:i+l] == pat):
            c += 1
    return c