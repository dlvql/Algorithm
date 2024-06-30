def solution(n):
    r, c = [1, 1]
    while True:
        c *= r
        if(c >= n):
            if(c > n):
                r -= 1
            break
        r += 1
    return r