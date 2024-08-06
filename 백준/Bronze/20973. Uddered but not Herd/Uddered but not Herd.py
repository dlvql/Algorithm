cow = input()
s = input()

idx = 0
cnt = 0

while idx < len(s):
  cnt += 1
  for i in cow:
    if idx == len(s): 
      break
    if s[idx] == i:
      idx += 1

print(cnt)