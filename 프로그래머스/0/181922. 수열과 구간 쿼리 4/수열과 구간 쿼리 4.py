def solution(arr, queries):
    for i in queries:
        s, e, k = i[0], i[1], i[2]
        for i in range(len(arr)):
            arr[i] += 1 if i <= e and i >= s and i % k == 0 else 0
    return arr