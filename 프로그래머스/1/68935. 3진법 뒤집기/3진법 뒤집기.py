def solution(n):
    thr = ''
    while n > 2:
        n, i = divmod(n, 3)
        thr += str(i)
    thr += str(n)
    return int(thr, 3)