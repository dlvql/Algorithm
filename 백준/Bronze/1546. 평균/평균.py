n = int(input())
arr = list(map(int, input().split()))

m = max(arr)
print(sum(list(map(lambda x: x / m * 100, arr))) / n)