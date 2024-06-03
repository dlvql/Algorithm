def solution(myStr):
    if set(myStr) == set(['a', 'b', 'c']):
        return ["EMPTY"]
    myStr = myStr.split('a')
    ans, ret = [], []
    for i in myStr:
        ans += i.split('b')
    for i in ans:
        ret += i.split('c')
    return list(filter(lambda x: x, ret))