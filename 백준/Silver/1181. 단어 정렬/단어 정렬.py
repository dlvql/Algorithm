n = int(input())
s = set()

for i in range(n):
    s.add(input())

s = sorted(s)
s = sorted(s, key = len)
print("\n".join(s))