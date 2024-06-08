def solution(picture, k):
    st = list()
    for i in picture:
        n = list()
        for s in i:
            n.append(s * k)
        st += ["".join(n)] * k
    return st