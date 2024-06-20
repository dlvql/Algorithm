def solution(price):
    if(price >= 500000):
        return price * 4 // 5
    elif(price >= 300000):
        return price * 9 // 10
    elif(price >= 100000):
        return price * 95 // 100
    else:
        return price