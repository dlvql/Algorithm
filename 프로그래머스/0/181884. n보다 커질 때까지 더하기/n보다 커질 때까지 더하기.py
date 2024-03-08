def solution(numbers, n):
    s = 0
    for i in numbers:
        if(s <= n):
            s += i
    return s