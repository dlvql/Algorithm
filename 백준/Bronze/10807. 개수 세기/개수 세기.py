n = int(input())
arr = list(map(int, input().split()))
v = int(input())

count = 0

for i in arr:
    count += 1 if i == v else 0

print(count)