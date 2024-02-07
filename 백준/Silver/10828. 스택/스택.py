import sys

n = int(sys.stdin.readline())
stack = list()

for i in range(n):
    command = sys.stdin.readline().strip()
    if(command.startswith('push')):
        stack.append(int(command.split()[1]))
    elif(command == 'pop'):
        sys.stdout.write(f'{stack.pop() if len(stack) > 0 else -1}\n')
    elif(command == 'size'):
        sys.stdout.write(f'{len(stack)}\n')
    elif(command == 'empty'):
        sys.stdout.write(f'{1 if len(stack) == 0 else 0}\n')
    else:
        sys.stdout.write(f'{stack[len(stack) - 1] if len(stack) > 0 else -1}\n')