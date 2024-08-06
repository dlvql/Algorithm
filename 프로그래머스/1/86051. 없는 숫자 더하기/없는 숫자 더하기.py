def solution(numbers):
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return sum(list(filter(lambda x: x not in numbers, s)))