def solution(n, k):
    return list(sorted(filter(lambda x: x % k == 0, list(range(1, n + 1)))))