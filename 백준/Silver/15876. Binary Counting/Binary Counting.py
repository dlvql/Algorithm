n, k = map(int, input().split())
b = ''

for i in range(1000):
  b += bin(i).split('0b')[1]

b = list(b)[k - 1::n]

print(" ".join(b[:5]))