def count(arr):
    for i in range(len(arr)):
        sumArr = 0
        for j in range(arr[i] + 1):
            sumArr += j
        arr[i] = sumArr
    return arr

cases = int(input())

for i in range(cases):
    arr = list(map(lambda x: len(x), list(filter(lambda x: len(x) > 0, input().split('X')))))
    print(sum(count(arr)))