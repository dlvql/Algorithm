import sys

n = int(sys.stdin.readline())
queue = list()

for i in range(n):
    command = sys.stdin.readline().strip()
    if(command.startswith('push')):
        queue.append(int(command.split()[1]))
    elif(command == 'pop'):
        sys.stdout.write(f'{queue.pop(0) if len(queue) > 0 else -1}\n')
    elif(command == 'size'):
        sys.stdout.write(f'{len(queue)}\n')
    elif(command == 'empty'):
        sys.stdout.write(f'{1 if len(queue) == 0 else 0}\n')
    elif(command == 'front'):
        sys.stdout.write(f'{queue[0] if len(queue) > 0 else -1}\n')
    else:
        sys.stdout.write(f'{queue[len(queue) - 1] if len(queue) > 0 else -1}\n')