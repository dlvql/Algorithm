while True:
    i = input()
    if(i == '0'):
        break
    if("".join(list(reversed(i))) == i):
        print('yes')
    else:
        print('no')