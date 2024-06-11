import sys
input = sys.stdin.readline
print = sys.stdout.write

for i in range(3):
  a = list(map(int, input().split()))
  ah = a[3] - a[0]
  am = a[4] - a[1]
  ase = a[5] - a[2]
  if(ase < 0):
    am -= 1
    ase += 60
  if(am < 0):
    ah -= 1
    am += 60
  print(f'{ah} {am} {ase}\n')
