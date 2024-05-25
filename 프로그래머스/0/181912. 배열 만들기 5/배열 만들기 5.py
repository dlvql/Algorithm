def solution(intStrs, k, s, l):
    return list(filter(lambda x: x > k, map(lambda x: int(x[s:s+l]), intStrs)))