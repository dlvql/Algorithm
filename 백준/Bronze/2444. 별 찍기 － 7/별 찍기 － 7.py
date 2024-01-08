n = int(input())

for i in range(n):
    arr = ""
    for j in range(n - i - 1):
        arr += " "
    for j in range((i + 1) * 2 - 1):
        arr += "*"
    print(arr)
for i in range(n - 1, 0, -1):
    arr = ""
    for j in range(n - i):
        arr += " "
    for j in range(i * 2 - 1):
        arr += "*"
    print(arr)