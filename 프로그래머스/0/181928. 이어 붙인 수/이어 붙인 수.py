def solution(num_list):
    return int("".join(map(str, list(filter(lambda x: x % 2 == 1, num_list))))) + int("".join(map(str, list(filter(lambda x: x % 2 == 0, num_list)))))