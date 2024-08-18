def solution(s):
    idx = 0
    ans = ''
    for w in s:
        if w == ' ':
            idx = 0
            ans += ' '
            continue
        if idx % 2 == 0:
            ans += w.upper()
        else:
            ans += w.lower()
        idx += 1
    return ans