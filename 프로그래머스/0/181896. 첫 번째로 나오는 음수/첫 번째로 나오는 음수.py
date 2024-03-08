def solution(num_list):
    li = list(filter(lambda x: x < 0, num_list))
    if(len(li) < 1):
        return -1
    else:
        return num_list.index(li[0])