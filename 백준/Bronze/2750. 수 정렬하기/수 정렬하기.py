import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readlines()))
lst.sort()

sys.stdout.write("\n".join(list(map(str, lst))))