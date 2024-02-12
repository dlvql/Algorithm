n = int(input())
for i in range(n):
    arr = input()
    if(len(arr) >= 6 and len(arr) <= 9):
        print("yes")
    else:
        print("no")