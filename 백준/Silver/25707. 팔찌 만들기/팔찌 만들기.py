n = int(input())
arr = list(sorted(map(int, input().split())))
arr = arr[:n // 2:-1] + arr[:n // 2 + 1]
ans = sum(map(lambda idx : abs(arr[idx - 1] - arr[idx]), range(n)))

print(ans)