def solution(b, y):
    s = b + y
    w, h = 0, 0
    for w in range(2, s + 1):
        if s % w != 0:
            continue
        h = s / w
        if (w - 2) * (h - 2) == y and b == s - y:
            if h > w:
                w, h = h, w
            break
    return [w, h]