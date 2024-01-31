N = int(input())
bongzis = [5, 3]


dp = [5001] * (N + 1)
dp[0] = 0

for bongzi in bongzis:
    for weight in range(bongzi, N + 1):
        dp[weight] = min(dp[weight], dp[weight - bongzi] + 1)

print(dp[N] if dp[N] != 5001 else -1)