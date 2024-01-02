arr = []

try:
    while True:
        arr.append(int(input()))
except Exception:
    newarr = sorted(arr)
    max = newarr[len(arr) - 1]
    print(f'{max}\n{arr.index(max) + 1}')