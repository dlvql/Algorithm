def solution(sides):
    a, b = sorted(sides)
    return len(range(b - a + 1, a + b))