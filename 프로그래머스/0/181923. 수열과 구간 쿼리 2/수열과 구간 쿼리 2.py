def solution(arr, queries):
    res = []
    for i in queries:
        s, e, k = i[0], i[1], i[2]
        tmp = list(sorted(filter(lambda x: x > k, arr[s : e + 1])))
        res.append(tmp[0] if tmp else -1)
    return res