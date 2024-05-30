def solution(num_list):
    c = 0
    for i in num_list:
        while i != 1:
            i = i / 2 if i % 2 == 0 else (i - 1) / 2
            c += 1
    return c