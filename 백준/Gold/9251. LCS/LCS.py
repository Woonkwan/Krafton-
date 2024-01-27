import sys
input = sys.stdin.readline

# 두 문자열 입력 받기
sudle = [input().strip() for _ in range(2)]

# 문자열의 길이에 맞게 DP 테이블 초기화
N, M = len(sudle[0]), len(sudle[1])
dp = [[0] * (M+1) for _ in range(N+1)]

# DP를 이용하여 LCS 계산
for i in range(1, N+1):
    for j in range(1, M+1):
        if sudle[0][i-1] == sudle[1][j-1]:
            # 문자가 일치하면 대각선 위의 값에 1을 더한다
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            # 문자가 일치하지 않으면, 왼쪽 또는 위쪽의 최대값을 가져온다
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 결과 출력 (DP 테이블의 마지막 값이 LCS의 길이)
print(dp[N][M])
