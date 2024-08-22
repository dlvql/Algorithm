def solution(sizes):
    sizes = list(map(lambda x: x if x[0] > x[1] else [x[1], x[0]], sizes))
    mw, mh = sizes[0]
    for i in sizes:
        mw = i[0] if i[0] > mw else mw
        mh = i[1] if i[1] > mh else mh
    return mw * mh