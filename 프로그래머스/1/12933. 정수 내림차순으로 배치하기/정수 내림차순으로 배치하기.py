def solution(n):
    n = list(map(int, list(str(n))))
    n.sort(reverse=True)
    n = list(map(str, n))
    return int("".join(n))