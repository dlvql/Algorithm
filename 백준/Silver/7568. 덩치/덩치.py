n = int(input())
arr = []
count = [1 for i in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

for i in range(n):
    for j in range(n):
        if(arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]):
            count[j] += 1

arr = sorted(count)

print(*count)