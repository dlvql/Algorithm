def check(x):
    if(x >= 50 and x % 2 == 0):
        return x / 2
    elif(x < 50 and x % 2 == 1):
        return x * 2 + 1
    else:
        return x

def solution(arr):
    c, bef = -1, []
    while bef != arr:
        bef = arr
        arr = list(map(check, arr))
        c += 1
    return c