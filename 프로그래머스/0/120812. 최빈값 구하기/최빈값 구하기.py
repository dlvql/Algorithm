def solution(array):
    di = dict(map(lambda x: [x, 0], array))

    for i in array:
        di[i] += 1

    m = [0, 0]
    for i in di:
        if m[1] < di.get(i):
            m[0] = i
            m[1] = di.get(i)

    if list(di.values()).count(m[1]) > 1:
        return -1

    else:
        return m[0]