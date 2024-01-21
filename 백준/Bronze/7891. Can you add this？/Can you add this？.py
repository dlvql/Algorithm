n = int(input())

for i in range(n):
    a, b = input().split()
    if('-' in a):
        a = int(a.replace('-', '')) * -1
    else:
        a = int(a)
    if('-' in b):
        b = int(b.replace('-', '')) * -1
    else:
        b = int(b)
    print(a + b)