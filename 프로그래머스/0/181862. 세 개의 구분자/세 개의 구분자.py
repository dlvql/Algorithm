def solution(myStr):
    myStr = list(filter(lambda x: x, myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()))
    return myStr if myStr else ["EMPTY"]