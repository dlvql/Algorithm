def solution(arr, n):
    m = 0
    if(len(arr) % 2 == 0): m = 1
    for i in range(len(arr) // 2 + (1 if len(arr) % 2 == 1 else 0)):
        arr[(i * 2 + m)] += n
    return arr