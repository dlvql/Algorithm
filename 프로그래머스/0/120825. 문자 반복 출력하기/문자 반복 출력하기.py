def solution(my_string, n):
    arr = []
    for i in my_string:
        arr += [i for _ in range(n)]
    return "".join(arr)