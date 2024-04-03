import sys

n = int(sys.stdin.readline())
skills = list(sys.stdin.readline())
contiguous = []
count = 0

for i in skills:
    if(i == 'R'):
        if('L' in contiguous):
            count += 1
            contiguous.remove('L')
        else: 
            break
    elif(i == 'K'):
        if('S' in contiguous):
            count += 1
            contiguous.remove('S')
        else:
            break
    elif(i == 'L' or i == 'S'):
        contiguous += i
    elif(i in list(map(str, range(1, 10)))):
        count += 1
    else:
        contiguous = []

sys.stdout.write(str(count))