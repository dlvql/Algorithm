A, B = [0, 0]

while True:
  cmd = input().split()
  if cmd[0] == '7':
    break
  if cmd[0] == '1':
    if cmd[1] == 'A':
      A = int(cmd[2])
    else:
      B = int(cmd[2])
  elif cmd[0] == '2':
    print(eval(cmd[1]))
  elif cmd[0] == '3':
    if cmd[1] == 'A':
      A += eval(cmd[2])
    else:
      B += eval(cmd[2])
  elif cmd[0] == '4':
    if cmd[1] == 'A':
      A *= eval(cmd[2])
    else:
      B *= eval(cmd[2])
  elif cmd[0] == '5':
    if cmd[1] == 'A':
      A -= eval(cmd[2])
    else:
      B -= eval(cmd[2])
  else:
    if cmd[1] == 'A':
      A //= eval(cmd[2])
    else:
      B //= eval(cmd[2])