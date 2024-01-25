N, M = map(int, input().split())
graph = [input() for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
#=================================================================================
def dfs(i, j, A):
    if 0 <= i < N and 0 <= j < M and graph[i][j] == A and not visited[i][j]:
        visited[i][j] = True
        if A == '-':
            dfs(i, j + 1, A)  #행일 때 돌고
        elif A == '|':
            dfs(i + 1, j, A)  #렬일 때 돌고
        return True
    return False
#=================================================================================

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == '-' or graph[i][j] == '|' and not visited[i][j]:
            if dfs(i, j, graph[i][j]):
                cnt += 1

print(cnt)
