sum = int(input())
cases = int(input())

total = 0

for i in range(cases):
    cost, count = map(int, input().split())
    total += cost * count

if(total == sum):
    print('Yes')
else:
    print('No')