import math

n, m = map(int, input().split())
package = 1000
bunches = 1000

for i in range(m):
    p, b = map(int, input().split())
    if(p < package):
        package = p
    if(b < bunches):
        bunches = b

print(min([math.ceil(n / 6) * package, n * bunches, n // 6 * package + n % 6 * bunches]))