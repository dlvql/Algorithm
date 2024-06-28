def solution(numbers, k):
    l = len(numbers)
    idx = 0
    for i in range(k - 1):
        idx += 2
        if(idx >= l):
            idx -= l
        # idx += 2 if (idx + 2) < len(numbers) else (2 - len(numbers))
    return numbers[idx]
        