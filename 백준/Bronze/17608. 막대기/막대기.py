import sys

n = int(sys.stdin.readline())
lst = []
ans = []
m = 0

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst = list(reversed(lst))

for i in lst:
    if(m < i):
        m = i
        ans.append(i)

sys.stdout.write(f'{len(ans)}')