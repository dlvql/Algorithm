t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    count = 1
    while(n > h):
        n -= h
        count += 1
    print(f'{n}{count:02d}')