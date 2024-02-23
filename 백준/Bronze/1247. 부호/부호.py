buho = []
for i in range(3):
    n = int(input())
    s = 0
    for j in range(n):
        s += int(input())
    buho += '+' if s > 0 else '-' if s < 0 else '0'

print("\n".join(buho))