def solution(n, slicer, num_list):
    a, b, c = slicer[0], slicer[1] + 1, slicer[2]
    if(n == 1):
        return num_list[:b]
    elif(n == 2):
        return num_list[a:]
    elif(n == 3):
        return num_list[a:b]
    else:
        return num_list[a:b:c]