import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr_n = [list(map(int, input().rstrip().split())) for _ in range(n)]
q = int(input().rstrip())
arr_q = [list(map(int, input().rstrip().split())) for _ in range(q)]

for i in arr_q:
  if i[0] == 1:
    p = arr_n[i[1] - 1].pop()
    arr_n[i[1] - 1].insert(0, p)
  elif i[0] == 2:
    new_arr_n = [[0 for _ in range(n)] for _ in range(n)]
    for idx in range(n):
      for jdx in range(n):
        new_arr_n[jdx][n - 1 - idx] = arr_n[idx][jdx]
    arr_n = new_arr_n[:]

sys.stdout.write("\n".join(list(map(lambda x: " ".join(map(str, x)), arr_n))))