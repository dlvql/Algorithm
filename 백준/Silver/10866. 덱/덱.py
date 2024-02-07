import collections
import sys

n = int(sys.stdin.readline())
deque = collections.deque()

for i in range(n):
    command = sys.stdin.readline().strip()
    if(command.startswith('push')):
        where = command.split('_')[1].split()[0]
        m = int(command.split('_')[1].split()[1])
        if(where == 'front'):
            deque.appendleft(m)
        else:
            deque.append(m)
    elif(command.startswith('pop')):
        where = command.split('_')[1]
        if(where == 'front'):
            sys.stdout.write(f'{deque.popleft() if len(deque) > 0 else -1}\n')
        else:
            sys.stdout.write(f'{deque.pop() if len(deque) > 0 else -1}\n')
    elif(command == 'size'):
        sys.stdout.write(f'{len(deque)}\n')
    elif(command == 'empty'):
        sys.stdout.write(f'{1 if len(deque) == 0 else 0}\n')
    elif(command == 'front'):
        sys.stdout.write(f'{deque[0] if len(deque) > 0 else -1}\n')
    else:
        sys.stdout.write(f'{deque[len(deque) - 1] if len(deque) > 0 else -1}\n')