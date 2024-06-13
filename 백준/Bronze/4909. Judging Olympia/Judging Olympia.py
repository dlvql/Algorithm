while True:
  ans = list(map(int, input().split()))
  if(all(i == 0 for i in ans)):
    break
  ans = sum(sorted(ans)[1:5])
  print(ans // 4 if ans % 4 == 0 else ans / 4)