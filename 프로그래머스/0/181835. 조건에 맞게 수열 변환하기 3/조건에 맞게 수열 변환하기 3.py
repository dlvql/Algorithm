def solution(arr, k):
    arr = list(map(lambda a : a * k, arr)) if k % 2 == 1 else list(map(lambda a : a + k, arr))
    return arr