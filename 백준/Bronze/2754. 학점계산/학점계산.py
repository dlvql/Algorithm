string = list(input())
count = 0

if(len(string) == 1):
    print('0.0')
else:
    if(string[0] == 'A'):
        count += 4.0
    elif(string[0] == 'B'):
        count += 3.0
    elif(string[0] == 'C'):
        count += 2.0
    elif(string[0] == 'D'):
        count += 1.0
    if(string[1] == '+'):
        count += 0.3
    elif(string[1] == '-'):
        count -= 0.3
    print(count)