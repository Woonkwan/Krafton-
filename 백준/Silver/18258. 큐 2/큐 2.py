import sys
from collections import deque


input = sys.stdin.readline

N = int(input().strip())

Q = deque()

for _ in range(N):
    command = input().split()

    if len(command) == 2:  
        Q.append(command[1])
    
    elif command[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    
    elif command[0] == 'size':
        print(len(Q))  
    
    elif command[0] == 'empty':
        print(1 if len(Q) == 0 else 0)
    
    elif command[0] == 'front':
        print(Q[0] if Q else -1)
        
    elif command[0] == 'back':
        print(Q[-1] if Q else -1)
