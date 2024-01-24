n, m = map(int, input().split())
narr = list(map(int, input().split()))
sarr = []

for i in range(n):
    for j in range(n):
        if(i == j):
            continue
        for k in range(n):
            if(i == k or j == k):
                continue
            sarr.append(narr[i] + narr[j] + narr[k])

if(m not in sarr):
    sarr = list(filter(lambda x: x < m, sarr))
    print(max(sarr))
else:
    print(m)