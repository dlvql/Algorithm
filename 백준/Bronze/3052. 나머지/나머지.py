arr = [int(input()) for i in range(10)]

arr = map(lambda x: x % 42, arr)

print(len(set(arr)))