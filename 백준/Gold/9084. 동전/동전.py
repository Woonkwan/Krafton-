def count(val, M):
    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in val:
        for i in range(coin, M + 1):
            dp[i] += dp[i - coin]

    return dp[M]

T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    coin_types = list(map(int, input().split()))
    goal = int(input())
    test_cases.append((coin_types, goal))

# 예제 출력
for coins, amount in test_cases:
    print(count(coins, amount))
