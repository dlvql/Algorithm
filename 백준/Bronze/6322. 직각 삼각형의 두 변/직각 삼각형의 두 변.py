idx = 0
answer = ""

while True:
  idx += 1
  arr = list(map(int, input().split()))
  if(all((i == 0) for i in arr)):
    break
  answer += f'Triangle #{idx}\n'
  if(arr[0] == -1):
    ans = arr[2] ** 2 - arr[1] ** 2
    if(ans <= 0):
      answer += "Impossible.\n\n"
      continue
    else:
      answer += f'a = {"%.3f" % (ans ** 0.5)}\n'
  elif(arr[1] == -1):
    ans = arr[2] ** 2 - arr[0] ** 2
    if(ans <= 0):
      answer += "Impossible.\n\n"
      continue
    answer += f'b = {"%.3f" % (ans ** 0.5)}\n'
  else:
    answer += f'c = {"%.3f" % ((arr[0] ** 2 + arr[1] ** 2) ** 0.5)}\n'
  answer += '\n'

print(answer.rstrip())