def solution(array, n):
    arr = list(map(lambda x: [x, abs(x - n)], array))
    arr.sort(key=lambda x: (x[1], x[0]))
    return arr[0][0]