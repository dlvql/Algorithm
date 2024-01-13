import math
x, y, w, h = map(int, input().split())
if(x > w - x):
    x = w - x
if(y > h - y):
    y = h - y
print(x if x < y else y)