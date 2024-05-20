import sys

h = int(sys.stdin.readline())

print('1' if h == 0 else ('0' if h == 1 else (('4' if h % 2 == 1 else '') + '8' * (h // 2))))