def solution(str_list):
    l, r = len(str_list), len(str_list)
    if("l" in str_list):
        l = str_list.index("l")
    if("r" in str_list):
        r = str_list.index("r")
    return str_list[:l] if l < r else str_list[r + 1:]