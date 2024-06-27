import math

l = int(input())
c = 0

for i in range(1, round(math.sqrt(l)) + 1):
    if(l % i == 0):
        c += i + (l // i)

print(c)