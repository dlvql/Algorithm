n = int(input())
for i in range(n):
  s = input()
  print(len(s[:s.index("D")]) if "D" in s else len(s))