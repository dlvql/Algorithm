k = int(input())
s = list(input().upper())
arr = []

for idx, i in enumerate(s):
  n = ord(i) - ((3 * (idx + 1)) + k)
  while n < 65 or n > 90:
    if n < 65 :
      n += 26
    if n > 90 :
      n -= 26
  arr.append(n)

print("".join(map(chr, arr)))