t = int(input())

def factorial(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

for i in range(t):
    n, m = map(int, input().split())
    s = factorial(m) / (factorial(m - n) * factorial(n))
    print(int(s))