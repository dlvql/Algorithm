a, b, c = int(input()), int(input()), int(input())
arr = list(str(a * b * c))
for i in range(10):
    print(arr.count(f'{i}'))