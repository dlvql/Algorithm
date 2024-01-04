a = int(input())
b = input()
listb = reversed(list(map(int, list(b))))

for i in listb:
    print(a * i)
print(a * int(b))