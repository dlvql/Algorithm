def solution(myString):
    return list(sorted(filter(lambda x: len(x) > 0, myString.split('x'))))