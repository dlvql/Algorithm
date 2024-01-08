def solution(arr):
    n = 0
    answer = []
    while True:
        if(n ** 2 >= arr):
            break
        else:
            n += 1
            if(arr % n == 0):
                answer.append(n)
                answer.append(int(arr / n))
    return sum(set(answer))