n, k = map(int, input().split())
arr = list(range(1, n + 1))
k -= 1
dele = k
ans = []

for i in range(n - 1):
    m = arr[dele]
    ans.append(m)
    arr.remove(m)
    dele = dele + k
    if(dele >= len(arr)):
        dele %= len(arr)

ans += arr

print(f'<{", ".join(map(str, ans))}>')