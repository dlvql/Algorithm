n = int(input())
times = list(map(int, input().split()))

youngsik = 0
minsik = 0

for i in times: 
    youngsik += (i // 30 + 1) * 10
    minsik += (i // 60 + 1) * 15

if(youngsik < minsik):
    print(f'Y {youngsik}')
elif(minsik < youngsik):
    print(f'M {minsik}')
else:
    print(f'Y M {youngsik}')