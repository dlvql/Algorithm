n, l, h = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

mid = arr[l:-h if h != 0 else len(arr)]

print(sum(mid) / len(mid))