arr = list(input().upper())
answer = [0 for i in range(26)]

for i in range(26):
#    if not(arr.in(chr(i + 65))):
    if not chr(i + 65) in arr:
        answer[i] = -1
    else:
        answer[i] = arr.index(chr(i + 65))
print(" ".join(list(map(str, answer))))