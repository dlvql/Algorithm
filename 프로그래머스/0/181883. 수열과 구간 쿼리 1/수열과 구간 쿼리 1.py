def solution(arr, queries):
    for i in queries:
        s, e = i
        arr = arr[:s] + list(map(lambda x: x + 1, arr[s:e+1])) + arr[e+1:]
    return arr