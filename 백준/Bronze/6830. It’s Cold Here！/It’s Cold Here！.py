import sys

lst = list(map(lambda x: [x.split()[0], int(x.split()[1])], sys.stdin.readlines()))
m = ['', 200]
for i in lst:
    if(m[1] > i[1]):
        m = i
sys.stdout.write(m[0])