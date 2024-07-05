import math
def solution(n):
    arr = []
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
            arr += [i, n // i] if n // i != i and n % i == 0 else [i] if n % i == 0 else []
    arr.sort()
    return arr