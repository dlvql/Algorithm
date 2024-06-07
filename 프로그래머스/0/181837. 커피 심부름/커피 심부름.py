def solution(order):
    return len(order) * 4500 + len(list(filter(lambda x: "latte" in x, order))) * 500