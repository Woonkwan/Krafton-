import sys
input = sys.stdin.readline

N, K = map(int, input().split())  #물건 수, K 가방 최대 무게, V 물건 가중치
items = [list(map(int, input().split())) for _ in range(N)]  #가방안의 아이템 무게[인덱스]에 따라 가중치 넣어줌

dp = [0] * ( K + 1 ) #[0, 0, 0,......... 0, 0]

for item in items:  #물건을 꺼내서 비교할거야!
    weight, V = item
    for i in range(K, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + V)

print(dp[-1])