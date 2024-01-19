t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    arr = []
    nextFloor = []
    for i in range(1, n + 1):
        arr.append(i)
        nextFloor.append(i)
    for i in range(k):
        for i in range(n):
            nextFloor[i] = sum(arr[0:i + 1])
        arr = nextFloor.copy()
    print(arr[n - 1])