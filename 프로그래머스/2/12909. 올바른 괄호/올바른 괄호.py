def solution(s):
    lst = list(s)
    stc = 0
    
    for i in lst:
        if(i == '('):
            stc += 1
        elif(stc < 1 and i == ')'):
            return False
        else:
            stc -= 1
    
    return True if stc == 0 else False