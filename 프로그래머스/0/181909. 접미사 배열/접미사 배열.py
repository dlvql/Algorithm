def solution(my_string):
    s = ''
    arr = []
    for i in list(my_string)[::-1]:
        s += i
        arr.append("".join(list(reversed(s))))
    arr.sort()
    return arr