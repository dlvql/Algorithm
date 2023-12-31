n, x = map(int, input().split())
arr = map(int, input().split())
output = ''
for i in filter(lambda e : e < x, arr):
    output += f'{i} '
print(output.rstrip())