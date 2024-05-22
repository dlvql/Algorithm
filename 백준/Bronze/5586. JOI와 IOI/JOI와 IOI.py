import sys

s = sys.stdin.readline()

ci = 0
for i in range(len(s) - 2):
  if(s[i] != 'I'):
    continue
  elif(s[i + 1] == 'O' and s[i + 2] == 'I'):
    ci += 1

sys.stdout.write(f'{s.count("JOI")}\n{ci}')