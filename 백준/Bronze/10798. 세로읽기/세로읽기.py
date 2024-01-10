arr = []
string = ''

for i in range(5):
    arr.append(list(input()))

for i in range(15):
    for j in range(len(arr)):
        if(i >= len(arr[j])):
            continue;
        string += arr[j][i]

print(string)