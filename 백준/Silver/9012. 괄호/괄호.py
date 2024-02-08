n = int(input())

for i in range(n):
    arr = list(input())
    hasPs = 0
    conPs = 0
    isValid = 1
    for e in arr:
        if(e == '('):
            hasPs = 1
            conPs += 1
        elif(e == ')' and hasPs != 1):
            isValid = 0
            break
        elif(e == ')' and hasPs == 1):
            conPs -= 1
            if(conPs == 0):
                hasPs = 0
            continue
    if(isValid == 1 and hasPs == 0):
        print('YES')
    else:
        print('NO')