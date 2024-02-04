from math import prod
l = prod(list(map(int, input().split())))
arr = list(map(int, input().split()))
arr = map(lambda x: x - l, arr)

print(*arr)