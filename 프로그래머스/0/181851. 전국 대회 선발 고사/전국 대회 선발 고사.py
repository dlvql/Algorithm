def solution(rank, attendance):
    available = []
    for idx, val in enumerate(attendance):
        if val:
            available.append((rank[idx], idx))
    available.sort()
    return 10000 * list(available[0])[1] + 100 * list(available[1])[1] + list(available[2])[1]