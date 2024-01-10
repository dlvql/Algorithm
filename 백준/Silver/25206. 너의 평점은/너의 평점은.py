sum = 0
haksum = 0
for i in range(20):
    arr = input().split()
    count = list(arr[2])
    gwapyung = 0
    if(count[0] == 'A'):
        gwapyung += 4.0
    elif(count[0] == 'B'):
        gwapyung += 3.0
    elif(count[0] == 'C'):
        gwapyung += 2.0
    elif(count[0] == 'D'):
        gwapyung += 1.0
    elif(count[0] == 'F'):
        haksum += float(arr[1])
        continue
    else:
        continue
    if(count[1] == '+'):
        gwapyung += 0.5

    gwahak = float(arr[1])
    sum += gwahak * gwapyung
    haksum += gwahak
if(haksum == 0):
    print(float(0))
else:
    print(sum / haksum)