n = input()
count = 0

if(int(n) % 7 == 0):
    count += 1
if("7" in n):
    count += 2

print(count)