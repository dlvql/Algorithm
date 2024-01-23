arr = input().rstrip()

dic = []

for i in range(1, len(arr) - 2):
    a = ''
    b = ''
    c = ''
    for j in range(i, len(arr) - 1):
        a = arr[:j]
        for k in range(j + 1, len(arr)):
            b = arr[j:k]
            c = arr[k:]
            dic.append("".join([a[::-1], b[::-1], c[::-1]]))
dic.sort()

print(dic[0])