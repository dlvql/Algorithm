a, b = map(int, input().split())
arr = []

for i in range(b + 1):
    for _ in range(i):
        arr.append(i)

print(sum(arr[a - 1 : b]))