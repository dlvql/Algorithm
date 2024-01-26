n, k = map(int, input().split())
l = k - 1 if k > 1 else 0

arr = [i for i in range(1, n + 1)]
ans = []

for i in range(1, n):
    now = arr[l]
    arr.remove(now)
    ans.append(now)
    l += k - 1
    l = l % len(arr) if l >= len(arr) else l

ans.append(arr[0])

ans = '<' + ", ".join(map(str, ans)) + '>'
print(ans)