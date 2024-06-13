k = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
queue = list()

def dfs(depth, now): # depth : 다음 인덱스, now: 연산값
  if(depth == k):
    queue.append(now)
    return
  dfs(depth + 1, now + arr[depth])
  dfs(depth + 1, now)
  dfs(depth + 1, now - arr[depth])
  return

dfs(0, 0)

print(s - len(list(set(filter(lambda x: x in range(1, s + 1), queue)))))