a = list(map(int, input().split()))
b = list(map(int, input().split()))

def f(x: list[int]): 
  return x[0] * 6 + x[1] * 3 + x[2] * 2 + x[3] + x[4] * 2

print(f(a), f(b))