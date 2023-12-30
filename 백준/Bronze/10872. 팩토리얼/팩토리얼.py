def factorial(idx):
    if(idx != 0):
        return idx * factorial(idx - 1)
    else:
        return 1

idx = int(input())
print(factorial(idx))