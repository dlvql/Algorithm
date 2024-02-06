y, m, d = map(int, input().split())
dy, dm, dd = map(int, input().split())

def isYun(year):
    if(year % 400 == 0):
        return True
    elif(year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

if(dy - y > 1000 or dy-y == 1000 and m <= dm and d <= dd):
    print("gg")
else:
    yearArr = list(range(y + 1, dy))
    monthArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthYunArr = monthArr.copy()
    monthYunArr[1] = 29
    dateSum = 0
    if(len(yearArr) >= 1):
        for i in yearArr:
            if(isYun(i)):
                dateSum += sum(monthYunArr)
            else:
                dateSum += sum(monthArr)
    if(y != dy):
        if(isYun(y) and m < 11):
            dateSum += sum(monthYunArr[m :]) + monthYunArr[m - 1] - d
        elif(not isYun(y) and m < 11):
            dateSum += sum(monthArr[m :]) + monthArr[m - 1] - d
        else:
            dateSum += 31 - d
        if(isYun(dy)):
            dateSum += sum(monthYunArr[:dm - 1]) + dd
        elif(not isYun(dy)):
            dateSum += sum(monthArr[:dm - 1]) + dd
    else:
        if(m == dm):
            dateSum += dd - d
        elif(isYun(y) and m <= 11 and dm <= 11):
            dateSum += sum(monthYunArr[m + 1 : dm]) + dd + monthYunArr[m - 1] - d
        elif(not isYun(y) and m <= 11 and dm <= 11):
            dateSum += sum(monthArr[m + 1 : dm]) + dd + monthArr[m - 1] - d
        else:
            if(isYun(y)):
                dateSum += dd + monthYunArr[m - 1] - d + sum(monthYunArr[m:10])
            else:
                dateSum += dd + monthArr[m - 1] - d + sum(monthArr[m:10])
    print(f'D-{dateSum}')