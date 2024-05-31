def solution(myString, pat):
    w = ''
    myString, pat = "".join(list(reversed(myString))), "".join(list(reversed(pat)))
    for i in range(len(myString)):
        if(myString[i] == pat[0]):
            w = "".join(list(reversed(myString[i:])))
            break
    return w