import math
month, dd, yyyy, time = input().split()

yyyy = int(yyyy)
isYun = True if yyyy % 400 == 0 or (yyyy % 4 == 0 and yyyy % 100 != 0) else False
monName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monDate = [31, 29 if isYun else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mm = monName.index(month) + 1
dd = int(dd.split(',')[0])
hour = int(time.split(':')[0])
minute = int(time.split(':')[1])

total = (366 if isYun else 365) * (24 * 60)

totalDate = sum(monDate[:mm - 1]) + dd - 1
print((((totalDate * 24 + hour) * 60) + minute) / total * 100)