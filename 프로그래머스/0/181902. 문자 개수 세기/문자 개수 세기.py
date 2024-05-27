def solution(my_string):
    arr = []
    for i in range(65, 91):
        arr.append(my_string.count(chr(i)))
    for i in range(97, 123):
        arr.append(my_string.count(chr(i)))
    return arr