def solution(n):
    cnt = 1
    for i in range(1, n + 1):
        s = 0
        for j in range(i, n + 1):
            if s == n:
                cnt += 1
                break
            elif s > n:
                break
            s += j
    return cnt