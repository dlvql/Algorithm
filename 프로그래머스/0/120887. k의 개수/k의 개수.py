def solution(i, j, k):
    return "".join(list(map(str, range(i, j + 1)))).count(str(k))