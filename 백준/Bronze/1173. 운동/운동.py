import sys

n, m, M, t, r = map(int, sys.stdin.readline().rstrip().split())
x = m
time = [0, 0]

if(m + t > M):
	time[1] = -1
else:
	while time[0] != n:
		if(x + t <= M):
				x += t
				time[0] += 1
				time[1] += 1
		elif(x <= M and x >= M - t and x >= m + r):
				x -= r
				time[1] += 1
		elif(x >= m and x <= m + r):
				x = m
				time[1] += 1
		else:
				time[1] = -1
				break

sys.stdout.write(f'{time[1]}')