def solution(k, score):
    ans = []
    m = []
    for i in score:
        m.append(i)
        m.sort(reverse=True)
        ans.append(m[(k - 1) if len(m) >= k else -1])
    return ans