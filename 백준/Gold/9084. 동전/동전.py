import sys
input = sys.stdin.readline

def all_coin_cnt(coin_types, moneys):
    dp = [0] * (moneys + 1)
    dp[0] = 1

    for coin in coin_types:
        for i in range(coin, moneys + 1):
            dp[i] += dp[i - coin]
    return dp[moneys]

T = int(input())
test_case = []

for _ in range(T):
    N = int(input())
    coin_type = list(map(int, input().split()))
    money = int(input())
    test_case.append((coin_type, money))

#출력
for coin_types, moneys in test_case:
    print(all_coin_cnt(coin_types,moneys))