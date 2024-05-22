def solution(l, r):
    ans = []
    i = 0
    for i in range(l, r + 1):
        if not set(str(i)) - set(['0', '5']):
            ans.append(i)
    return ans if ans else [-1]