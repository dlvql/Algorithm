def solution(a, d, included):
    res = 0

    for i in range(len(included)):
        if(included[i] == True):
            res += i * d + a

    return res