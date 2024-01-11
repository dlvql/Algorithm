n = int(input())

def toZero(arr):
    count = 0
    for i in arr:
        if(i != '0'):
            return count
        count += 1

facto = 1

for i in range(1, n + 1):
    facto *= i

answer = list(reversed(str(facto)))
print(toZero(answer))