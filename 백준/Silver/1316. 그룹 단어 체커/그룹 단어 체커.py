n = int(input())
count = 0
boolean = False

for i in range(n):
    arr = input()
    length = len(arr)
    answer = set()
    for j in range(length):
        if(arr[j] in answer and arr[j - 1] != arr[j]):
            boolean = False
            break
        else:
            answer.add(arr[j])
        boolean = True
    if(boolean == True):
        count += 1
print(count)