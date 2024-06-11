import sys

n, w, h, l = map(int, sys.stdin.readline().split())
c = (w // l) * (h // l)

sys.stdout.write(f'{c if c < n else n}')