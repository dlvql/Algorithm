n = int(input())
files = list(map(int, input().split()))
c = int(input())

used = 0

for i in files:
    used += c * (i // c) + (c if i % c != 0 else 0)

print(used)