def solution(myString):
    # return "".join([("A" if s == "a" else s.lower()) for s in myString])
    answer = []
    for i in myString:
        answer.append("A" if i == "a" or i == "A" else i.lower())
    return "".join(answer)