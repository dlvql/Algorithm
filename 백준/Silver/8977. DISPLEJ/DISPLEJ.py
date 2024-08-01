n, k, b = map(int, input().split())
arr = list(map(int, input().split()))

idx = b % n - 1
s = 0

for i in range(k):
  s += arr[(idx + i) % n]

print(s)