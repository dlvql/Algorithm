def solution(a, b, c, d):
    s = list(set(map(lambda x: (x, [a, b, c, d].count(x)), [a, b, c, d])))
    s.sort(key=lambda x: (-list(x)[1]))

    if(len(s) == 1):
        return list(s[0])[0] * 1111
    elif(len(s) == 2):
        p, q = list(s[0]), list(s[1])
        if(p[1] == 2):
            return (p[0] + q[0]) * abs(p[0] - q[0])
        else:
            return (10 * p[0] + q[0]) ** 2
    elif(len(s) == 3):
        q, r = filter(lambda x: list(x)[1] == 1, s)
        return list(q)[0] * list(r)[0]
    else:
        return list(min(s))[0]