n = int(input())
m = int(input())
arr = list(map(int, input().split())) # arr[i]의 값은 i번째 게임의 타겟을 의미
score = [0 for i in range(n)]

for i in range(m):
  game = list(map(int, input().split()))
  for idx in range(n):
    if(game[idx] == arr[i]):
      # print(f"now game: {i}th / get score : {idx} / target: {arr[i]}")
      score[idx] += 1
    else:
      # print(f"now game: {i}th / target {arr[i]} get score")
      score[arr[i] - 1] += 1

for i in score:
  print(i)