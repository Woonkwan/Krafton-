import sys

stack = []

N = int(sys.stdin.readline())

for _ in range(N):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack:
            sys.stdout.write(stack.pop() + '\n')
        else:
            sys.stdout.write('-1\n')
    elif command[0] == 'size':
        sys.stdout.write(str(len(stack)) + '\n')
    elif command[0] == 'empty':
        sys.stdout.write('0\n' if stack else '1\n')
    elif command[0] == 'top':
        if stack:
            sys.stdout.write(stack[-1] + '\n')
        else:
            sys.stdout.write('-1\n')
