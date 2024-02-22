n, m = map(int, input().split())
arr = []
countN = set()
countM = set()

for i in range(n):
    countN.add(i)
for i in range(m):
    countM.add(i)

for i in range(n):
    arr = list(input())
    for j in range(m):
        if(arr[j] == 'X'):
            countN.discard(i)
            countM.discard(j)

print(len(countN) if len(countN) > len(countM) else len(countM))