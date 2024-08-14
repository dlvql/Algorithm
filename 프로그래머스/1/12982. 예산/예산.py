def solution(d, budget):
    cnt = 0
    d.sort()
    for i in d:
        if budget < i:
            break
        budget -= i
        cnt += 1
    return cnt