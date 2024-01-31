import sys
input = sys.stdin.readline

N, K = map(int, input().split())
W_V = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1) 

for item in W_V:
    W, V = item
    for i in range(K, W - 1, -1): #K부터 (W-1)까지 -1씩 감소
        dp[i] = max(dp[i], dp[i - W] + V)

print(dp[-1])