import sys
n = int(sys.stdin.readline().strip())
f = int(sys.stdin.readline().strip())
pl = n + 100 - (n + 100) % 100
n = n - (n % 100)

m = 99
if(n % f != 0):
    n = n - n % f if n - n % f >= n - n % 100 else n + f - n % f

while n < pl:
    if(m > n % f):
        m = n % f
    if(m == 0):
        break
    else:
        n += f

sys.stdout.write(f'{"".join(list(reversed(str(n)[-1:-3:-1]))).zfill(2)}')