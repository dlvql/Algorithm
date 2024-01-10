maxValue = 0
maxX, maxY = 1, 1 # 행 열

for i in range(9):
    scan = list(map(int, input().split()))
    if(max(scan) > maxValue):
        maxValue = max(scan)
        maxX = i + 1
        maxY = scan.index(maxValue) + 1 if scan.index(maxValue) != 9 else 9

print(maxValue)
print(maxX, maxY)