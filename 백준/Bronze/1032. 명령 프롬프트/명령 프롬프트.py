n = int(input())
last = list(input())
arr = [1 for _ in range(len(last))]

for i in range(n - 1):
    st = list(input())
    for j in range(len(last)):
        arr[j] = 1 if last[j] == st[j] and arr[j] == 1 else 0
    last = st

answer = ''
for i in range(len(arr)):
    answer += last[i] if arr[i] == 1 else '?'

print(answer)