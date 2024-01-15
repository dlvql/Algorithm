stick = [64]
length = int(input()) # 64보다 작거나 같은 자연수
while sum(stick) > length:
    a = min(stick)
    stick.remove(a)
    a /= 2
    stick += [a, a]
    if(sum(stick) - a >= length):
        stick.pop()
print(len(stick))