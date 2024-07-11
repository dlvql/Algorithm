def solution(p):
    arr = []
    p = p.split(' + ')
    x_list = list(filter(lambda x: "x" in x, p))
    for idx, i in enumerate(x_list):
        x_list[idx] = i.replace('x', '')
        if(x_list[idx] == ''):
            x_list[idx] = '1'
    x = sum(list(map(int, x_list)))
    n = sum(list(map(int, filter(lambda x: x.isdigit(), p))))
    arr.append(f'{x}x' if x > 1 else 'x' if x == 1 else '')
    arr.append(str(n) if n > 0 else '')
    return " + ".join(list(filter(lambda x: x, arr)))