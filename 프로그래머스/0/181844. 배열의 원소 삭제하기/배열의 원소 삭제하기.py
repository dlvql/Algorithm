def solution(arr, delete_list):
    for i in delete_list:
        arr.remove(i) if i in arr else next
    return arr