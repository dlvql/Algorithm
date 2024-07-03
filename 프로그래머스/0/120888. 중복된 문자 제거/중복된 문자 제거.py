def solution(my_string):
    s = set()
    arr = ""
    for i in my_string:
        if i not in s:
            s.add(i)
            arr += i
    return arr