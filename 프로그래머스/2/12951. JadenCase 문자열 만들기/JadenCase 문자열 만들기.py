def solution(s):
    s = list(s)
    arr = [s[0].upper()]
    for idx, v in enumerate(s[1:]):
        arr.append(v.lower() if s[idx] != " " else v.upper())
    return "".join(arr)