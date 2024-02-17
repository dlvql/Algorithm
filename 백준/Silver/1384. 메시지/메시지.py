count = 0
while True:
    count += 1
    n = int(input())
    if(n == 0):
        break
    print(f"Group {count}")
    name = []
    nasty = []
    for i in range(n):
        arr = input().split()
        name.append(arr[0])
        nasty += arr[1:]
    if(nasty.count('N') == 0):
        print("Nobody was nasty")
    else:
        for i in range(len(nasty)):
            if(nasty[i] == 'N'):
                mess = ((i // (n - 1)) - (i % (n - 1) + 1))
                print(f'{name[mess if mess >= 0 else mess + n]} was nasty about {name[i // (n - 1)]}')
    print("")