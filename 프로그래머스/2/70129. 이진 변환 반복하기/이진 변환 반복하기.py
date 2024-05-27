def solution(s):
    arr = []
    c = 0
    while s != "1" :
        arr.append(s.count("0"))
        s = str(bin(s.count("1")))[2:]
        c += 1
    return [c, sum(arr)]