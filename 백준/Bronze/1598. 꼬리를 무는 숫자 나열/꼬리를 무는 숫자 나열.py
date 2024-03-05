a, b = map(int, input().split())

sn = abs((4 if a % 4 == 0 else a % 4) - (4 if b % 4 == 0 else b % 4))
ew = abs((a // 4 + (1 if a % 4 != 0 else 0)) - (b // 4 + (1 if b % 4 != 0 else 0)))

print(sn + ew)