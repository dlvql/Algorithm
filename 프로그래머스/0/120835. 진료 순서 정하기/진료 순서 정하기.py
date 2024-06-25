def solution(emergency):
    em = list(sorted([(i, v) for i, v in enumerate(emergency)], key=lambda x: list(x)[1], reverse=True))
    arr = [0 for _ in emergency]
    for i, v in em:
        arr[i] = em.index((i, v)) + 1
    return arr