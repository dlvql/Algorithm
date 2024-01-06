h, m = map(int, input().split())
m += int(input())
while(m >= 60):
    m -= 60
    h += 1
if(h >= 24):
    h -= 24
print(f'{h} {m}')