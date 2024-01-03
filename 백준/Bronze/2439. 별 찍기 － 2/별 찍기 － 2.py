n = int(input())
for i in range(n):
    arr = ''
    for j in range(1, n - i):
        arr += ' '
    for j in range(i + 1):
        arr += '*'
    print(arr)