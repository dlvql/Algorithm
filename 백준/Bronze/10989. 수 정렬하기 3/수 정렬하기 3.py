import sys

n = int(sys.stdin.readline().rstrip())
arr = [0 for _ in range(10000)]

for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    arr[m - 1] += 1

for i in range(10000):
    for j in range(arr[i]):
        sys.stdout.write(f'{i + 1}\n')