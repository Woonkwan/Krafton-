import sys
input = sys.stdin.readline

N = int(input())
gameBoard = []

for _ in range(N):
    gameBoard.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1  # 시작점

for row in range(N):
    for col in range(N):
        jump = gameBoard[row][col]
        if jump > 0:
            if row + jump < N:
                dp[row + jump][col] += dp[row][col]
            if col + jump < N:
                dp[row][col + jump] += dp[row][col]

print(dp[N-1][N-1])
