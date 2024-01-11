from operator import itemgetter

n = int(input())
arr = []

for i in range(n):
    member = input().split()
    member[0] = int(member[0])
    arr.append(tuple(member))

arr = sorted(arr, key=itemgetter(0))

for i in arr:
    print(*list(i))