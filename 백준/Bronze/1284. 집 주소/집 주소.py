while True:
    n = list(input())
    if(n[0] == '0'):
        break
    hap = len(n) + 1
    for i in n:
        if(i == '0'):
            hap += 4
        elif(i == '1'):
            hap += 2
        else:
            hap += 3
    print(hap)