n, m = map(int, input().split())

arrA = list() 
arrB = list()

for i in range(n):
    arrA.append(list(map(int, input().split())))
for i in range(n):
    arrB.append(list(map(int, input().split())))

for i in range(n):
    result = ''
    for j in range(m):
        result += f'{arrA[i][j] + arrB[i][j]} '
    print(result.rstrip())