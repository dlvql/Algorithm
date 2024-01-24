import math
n, m = map(int, input().split())

gongyaksu = 1
gongbaesu = n * m

def yaksu(x):
    arr = []
    n = math.sqrt(x)
    for i in range(1, math.ceil(n) + 1):
        if(x % i == 0):
            arr += [i, x // i]
    arr.sort()
    return arr

def baesu(x):
    arr = []
    maxBaesu = n * m
    for i in range(1, maxBaesu // x):
        arr.append(i * x)
    return arr

nyaksu = yaksu(n)
myaksu = yaksu(m)
nbaesu = baesu(n)
mbaesu = baesu(m)

for i in nyaksu:
    if(i in myaksu):
        gongyaksu = i
for i in nbaesu:
    if(i in mbaesu):
        gongbaesu = i
        break

print(gongyaksu)
print(gongbaesu)