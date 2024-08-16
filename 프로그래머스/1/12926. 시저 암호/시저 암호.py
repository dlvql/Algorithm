def solution(s, n):
    ans = ''
    for i in s:
        if i == ' ':
            ans += i
            continue
        v = ord(i)
        if (v < 91 and v + n > 90) or (v + n) > 122:
            v -= 26
        ans += chr(v + n)
    return ans