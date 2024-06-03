def solution(arr, k):
    l = list(dict.fromkeys(arr))[:k]
    return l if len(l) == k else (l + ([-1] * (k - len(l))))