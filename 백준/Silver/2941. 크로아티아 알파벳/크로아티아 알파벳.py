arr = input()
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in alphabet:
    while True:
        if(i not in arr):
            break
        else:
            arr = arr.replace(i, "a")

print(len(arr))