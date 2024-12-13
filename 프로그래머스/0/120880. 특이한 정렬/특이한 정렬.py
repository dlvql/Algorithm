def solution(numlist, n):
    ans = []
    abss = []
    for i in range(len(numlist)):
        a = set([i, n - numlist[i]])
        abss.append([i, n - numlist[i]])
    abss.sort(key=lambda x: (abs(x[1]), x[1]))
    for i in abss:
        ans.append(numlist[i[0]])
    return ans