import sys
input = sys.stdin.readline

def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * len(p) for _ in range(len(p))]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]

# 입력
N = int(input())
hang = [list(map(int, input().split())) for _ in range(N)]

# 각 행렬의 행과 열 크기를 순서대로 배열에 저장
p = [hang[0][0]] + [sizes[1] for sizes in hang]
# p = [hang[0][0]]
# for i in hang:
#     p.append(i[1])
# 과 같은표현

# 결과 출력
print(matrix_chain_order(p))