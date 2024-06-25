def solution(rsp):
    s = ''
    for i in rsp:
        s += '0' if i == '2' else '5' if i == '0' else '2'
    return s