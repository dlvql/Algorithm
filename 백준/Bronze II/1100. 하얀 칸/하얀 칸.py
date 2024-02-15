count = 0

for i in range(8):
    chess = list(input())
    for j in range(8):
        if(i % 2 == 0 and j % 2 == 0 and chess[j] == 'F'):
            count += 1
        elif(i % 2 == 1 and j % 2 == 1 and chess[j] == 'F'):
            count += 1

print(count)