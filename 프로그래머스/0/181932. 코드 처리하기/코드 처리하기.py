def solution(code):
    ret = ''
    mode = "0"
    for idx in range(len(code)):
        if(code[idx] != "1" and idx % 2 == int(mode)):
            ret += code[idx]
        elif(code[idx] == "1"):
            mode = "0" if mode == "1" else "1"
    return ret if ret != '' else "EMPTY"