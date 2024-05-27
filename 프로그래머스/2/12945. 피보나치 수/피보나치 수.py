def solution(n):
    s, c, arr = 1, 0, [0, 1]
    while c < n - 1:
        s += arr[c]
        c += 1
        arr.append(s)
    return arr[-1] % 1234567