while True:
    arr = list(map(int, input().split()))
    if(arr == [0, 0, 0]):
        break;
    arr = sorted(arr)
    arr = list(map(lambda x: x ** 2, arr))
    if(arr[0] + arr[1] == arr[2]):
        print("right")
    else:
        print("wrong")