n = int(input())

dif = n % 5

if(n < 3):
    print("-1")
elif(dif == 0):
    print(n // 5)
elif(dif == 1 or dif == 3):
    print(n // 5 + 1)
elif(dif == 2):
    if(n < 12):
        print("-1")
    else:
        print((n - 12) // 5 + 4)
elif(dif == 4):
    if(n < 9):
        print("-1")
    else:
        print((n - 9) // 5 + 3)
else:
    print("-1")