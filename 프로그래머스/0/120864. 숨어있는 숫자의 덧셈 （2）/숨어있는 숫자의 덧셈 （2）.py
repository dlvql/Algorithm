def solution(my_string):
    n = 0
    arr = ''
    for i in list(my_string.upper()):
        if ord(i) <= 90 and ord(i) > 64:
            arr += ' '
        else:
            arr += i
    return sum([int(i) for i in arr.split()])