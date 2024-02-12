import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
X = str(A*B*C)

# print(X[0])
for j in range(10):
    cnt = 0
    for i in range(len(X)):        
        if X[i] == str(j):
            cnt += 1
    print(cnt)