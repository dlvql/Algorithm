def solution(numbers):
    numbers.sort()
    p = numbers[-1] * numbers[-2]
    n = numbers[0] * numbers[1]
    return p if p >= n else n