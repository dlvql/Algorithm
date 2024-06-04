def solution(n):
    cnt = str(bin(n)).count("1")
    new = 0
    num = n
    while cnt != new:
        num += 1
        new = str(bin(num)).count("1")
    return num