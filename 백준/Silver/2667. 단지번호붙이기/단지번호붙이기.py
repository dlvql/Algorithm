import sys
from collections import deque

n = int(sys.stdin.readline())
li = list()
dq = deque()
cnt = 0
danji = deque()

for i in range(n):
  li.append(list(map(int, list(sys.stdin.readline().rstrip('\n')))))

cp = li.copy()

x = [1, 0, -1, 0]
y = [0, 1, 0, -1]

def bfs():
  cnt = 1
  while len(dq) > 0:
    tmp = dq.popleft()
    cp[tmp[0]][tmp[1]] = 0
    for i in range(4):
      x_ = tmp[0] + x[i]
      y_ = tmp[1] + y[i]
      if(0 <= x_ < n and 0 <= y_ < n and cp[x_][y_] == 1):
        dq.append((x_, y_))
        cp[x_][y_] = 0
        cnt += 1
  danji.append(cnt)

for i in range(n):
  cnt = 0
  for j in range(n):
    if (cp[i][j] == 1):
      dq.append((i, j))
      bfs()

danji = deque(sorted(list(danji)))
danji.appendleft(len(danji))

sys.stdout.write("\n".join(map(str, danji)))