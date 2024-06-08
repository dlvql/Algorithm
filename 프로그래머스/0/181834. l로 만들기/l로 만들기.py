def solution(myString):
    return "".join(list(map(lambda x: "l" if x < 108 else chr(x), map(ord, list(myString)))))