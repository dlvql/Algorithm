def solution(s):
    arr = []
    for i in set(s):
        if(s.count(i) == 1):
            arr.append(ord(i))
    arr = list(sorted(map(lambda x: chr(x), arr)))
    return "".join(arr)