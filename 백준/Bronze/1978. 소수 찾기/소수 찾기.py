n = int(input())
arr = list(map(int, input().split()))
count = 0

def prime(x):
    boolean = False
    for i in range(2, x + 1):
        if(i ** 2 > x):
            return boolean
        elif(x % i == 0):
            return False
        else:
            boolean = True

for i in arr:
    if(prime(i) == True or i in [2, 3]):
        count += 1
print(count)