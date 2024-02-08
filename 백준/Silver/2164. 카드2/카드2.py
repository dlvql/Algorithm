import sys
import collections

n = int(sys.stdin.readline().strip())
arr = collections.deque(range(1, n + 1))

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())

sys.stdout.write(f'{arr[0]}')