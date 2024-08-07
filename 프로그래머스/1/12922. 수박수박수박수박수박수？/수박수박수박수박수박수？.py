def solution(n):
    s = ['수', '박']
    ans = ''
    for i in range(n):
        ans += s[i % 2]
    return ans