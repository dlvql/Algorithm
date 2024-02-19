n = int(input())
arr = []
answer = set()

for i in range(n):
    arr.append(list(input())[0])

for i in arr:
    if(arr.count(i) >= 5):
        answer.add(i)

if(len(answer) == 0):
    print("PREDAJA")
else:
    print("".join(list(sorted(answer))))