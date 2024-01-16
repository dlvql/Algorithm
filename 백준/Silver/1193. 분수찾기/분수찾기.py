n = int(input())
sum = 0
count = 0
for i in range(n + 1):
    sum += i
    count += 1
    if(sum >= n):
        sum -= i
        break
if(count %2 == 0):
    print(f'{sum - n + count}/{n - sum}')
else:
    print(f'{n - sum}/{sum - n + count}')