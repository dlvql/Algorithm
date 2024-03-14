def solution(my_strings, parts):
    return "".join([my_strings[s][parts[s][0]:parts[s][1] + 1] for s in range(len(my_strings))])