n = int(input())
s = input().replace(' ', '').replace(',', '').replace('.', '')
maxCount = []

for i in range(26):
  maxCount.append(s.count(chr(i + 97)))

print(max(maxCount))