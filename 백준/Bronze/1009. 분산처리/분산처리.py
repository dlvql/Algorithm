import sys
n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10
    if(a == 2 or a == 3 or a == 7 or a == 8):
        b = b % 4
        if(b == 0):
            b = 4
    elif(a == 4 or a == 9):
        b = b % 2
        if(b == 0):
            b = 2
    else:
        b = 1
    datas = 10 if (a ** b) % 10 == 0 else (a ** b) % 10
    sys.stdout.write(f'{datas}\n')