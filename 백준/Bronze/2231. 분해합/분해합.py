import math
n = int(input())
sum = 0

for i in range(n):
    sum += i
    this = i
    while this > 0:
        sum += this % 10
        this = math.floor(this / 10)
    if(sum == n):
        sum = i
        break
    sum = 0

print(sum)