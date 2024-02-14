a, b = map(int, input().split())

if(a != b and (a + b) % 2 == 1 or a < b or a < 0 or b < 0):
    print('-1')
else:
    print(int((a + b) / 2), int((a - b) / 2))