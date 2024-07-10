def solution(keyinput, board):
    x, y = map(lambda n: (n - 1) // 2, board)
    s, g = [0, 0]
    for i in keyinput:
        if i == "up":
            s += 1 if s < y else 0
        elif i == "down":
            s -= 1 if s > -y else 0
        elif i == "left":
            g -= 1 if g > -x else 0
        else:
            g += 1 if g < x else 0
    return [g, s]