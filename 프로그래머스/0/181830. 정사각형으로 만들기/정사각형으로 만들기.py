def solution(arr):
    arrlen = len(arr[0])
    if(arrlen <= len(arr)):
        arr = list(map(lambda x: x + [0] * (len(arr) - arrlen), arr))
    else:
        zeros = [0] * arrlen
        arr += [zeros] * (arrlen - len(arr))
    return arr