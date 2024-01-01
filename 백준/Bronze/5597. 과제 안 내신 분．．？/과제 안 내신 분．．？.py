arr = set()
count = 0
for i in range(28):
    arr.add(int(input()))

answerArr = set(range(1, 31)) - arr
arr = list()

for i in range(2):
    arr.append(answerArr.pop())
arr = sorted(arr)
for i in range(2):
    print(arr[i])