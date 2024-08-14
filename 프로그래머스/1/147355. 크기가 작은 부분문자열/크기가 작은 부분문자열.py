def solution(t, p):
    l = len(p)
    p = int(p)
    cnt = 0
    for idx in range(len(t) - l + 1):
        if int(t[idx:idx + l]) <= p:
            cnt += 1
    return cnt