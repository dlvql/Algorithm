import heapq

def solution(sco, k):
    cnt = 0
    heapq.heapify(sco)
    while any(filter(lambda x: x < k, sco)):
        if (len(sco) == 1) or (len(sco) < 3 and sco[0] * 2 + sco[1] < k):
            return -1
        heapq.heappush(sco, heapq.heappop(sco) + (heapq.heappop(sco) * 2))
        cnt += 1
    return cnt