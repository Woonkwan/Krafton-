import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    ave = 0
    chk = 0
    X = input().split()
    for i in range(1, len(X)):
        ave += int(X[i])
    ave = ave // int(X[0])
    for i in range(1, len(X)):
        if int(X[i]) > ave:
            chk += 1
    chk = chk / int(X[0]) * 100.0
    print(f"{chk:.3f}%")