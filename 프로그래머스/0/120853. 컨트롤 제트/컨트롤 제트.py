def solution(s):
    arr = s.split()
    last = 0
    r = 0
    for i in arr:
        if(i.isdigit() or '-' in i):
            last = int(i)
            r += last            
        else:
            r -= last
    return r