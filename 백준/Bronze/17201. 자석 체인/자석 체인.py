n = int(input())
m = list(input())

r = 'Yes'

for idx, a in enumerate(m[:-1]):
  if(m[idx + 1] == a):
    r = 'No'
    break

print(r)