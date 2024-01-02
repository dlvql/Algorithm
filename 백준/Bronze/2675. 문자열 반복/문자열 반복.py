n = int(input())
for i in range(n):
    inp = input().split(' ')
    r, s = int(inp[0]), inp[1]
    arr = []
    for j in range(len(s)):
        for k in range(r):
            arr.append(s[j])
    print("".join(arr))