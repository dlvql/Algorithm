def solution(a, b):
    cnt = 0
    while a != b:
        if cnt >= len(b):
            cnt = -1
            break
        a = a[-1] + a[:-1]
        cnt += 1
    return cnt