n = int(input())

for i in range(n):
    string = ''
    for j in range(n, i, -1):
        string += '*'
    print(string)