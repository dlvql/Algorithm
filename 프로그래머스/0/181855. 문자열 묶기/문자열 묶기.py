def solution(strArr):
    strArr.sort(key=len)
    mx = [0] * (len(strArr[-1]) + 1)
    for i in strArr:
        mx[len(i)] += 1
    mx.sort()
    return mx[-1]