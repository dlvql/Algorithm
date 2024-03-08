def solution(n, control):
    li = list(control)
    for i in li:
        if(i == 'w'):
            n += 1
        elif(i == 's'):
            n -= 1
        elif(i == 'd'):
            n += 10
        elif(i == 'a'):
            n -= 10
    return n