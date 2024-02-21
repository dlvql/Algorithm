a, b = map(list, input().split())
a = list(map(int, a))
b = list(map(int, b))

sum = 0

for i in a:
    for j in b:
        sum += i*j

print(sum)