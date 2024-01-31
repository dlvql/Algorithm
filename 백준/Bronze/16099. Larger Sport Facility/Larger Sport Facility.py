n = int(input())

for i in range(n):
    lt, wt, le, we = map(int, input().split())
    t, e = lt * wt, le * we
    if(t > e):
        print("TelecomParisTech")
    elif(e > t):
        print("Eurecom")
    else:
        print("Tie")