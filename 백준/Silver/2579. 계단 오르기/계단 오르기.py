import sys
input = sys.stdin.readline

N = int(input())
stairs = [0 for _ in range(301)]
DP = [0 for _ in range(301)]

for i in range(N):
    stairs[i] = int(input())
    DP[0] = stairs[0]
    DP[1] = max(stairs[0] + stairs[1], stairs[1])
    DP[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, N + 1):
        DP[i] = max(DP[i-3] + stairs[i-1] + stairs[i], DP[i-2] + stairs[i])

print(DP[N-1])