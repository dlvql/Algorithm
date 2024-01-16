a, b, n = map(int, input().split())
mo = 0

for i in range(n + 1):
    mo = a // b
    a = a % b * 10

print(mo)