import sys

input = sys.stdin.readline
print = sys.stdout.write

a, p, c = map(int, input().split())

print(f'{a + c if a + c > p else p}')