def solution(my_string):
    c = 0
    for i in my_string:
        if(i.isdigit()):
            c += int(i)
    return c