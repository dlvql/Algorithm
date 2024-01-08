count = list(map(int, input().split()))
arr = [1, 1, 2, 2, 2, 8]
answer = []

for i in range(6):
    answer += [arr[i] - count[i]]
    
print(*answer)