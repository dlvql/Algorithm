import sys

n = int(sys.stdin.readline())
before = sys.stdin.readline().rstrip()
after = sys.stdin.readline()

ans = 0

for i in range(len(before)):
  if((before[i] == after[i] and n % 2 != 0) or (before[i] != after[i] and n % 2 == 0)):
    ans = 1
    break

sys.stdout.write("Deletion failed" if ans == 1 else "Deletion succeeded")