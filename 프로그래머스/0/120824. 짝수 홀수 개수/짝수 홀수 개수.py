def solution(num_list):
    arr = [0, 0]
    for i in num_list:
        arr[i % 2] += 1
    return arr