def solution(quiz):
    arr = []
    for i in quiz:
        e, r = i.split("=")
        arr.append("O" if eval(e.strip()) == int(r.strip()) else "X")
    return arr