def solution(arr):
    answer = []
    for i in arr:
        answer.append(i // 2 if i >= 50 and i % 2 == 0 else (i * 2 if i < 50 and i % 2 == 1 else i))
    return answer