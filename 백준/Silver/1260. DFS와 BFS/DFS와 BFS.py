from collections import deque

def dfs(graph, v, visited1):
    visited1[v] = True
    print(v, end=' ')  # 방문한 노드 출력

    for i in graph[v]:
        if not visited1[i]:
            dfs(graph, i, visited1)

#---------------------------------------------------------------
def bfs(graph, v, visited2):

    q = deque([v])

    while q:
        v = q.popleft()
        if not visited2[v]:
            visited2[v] = True
            print(v, end=" ")
            for i in graph[v]:
                if not visited2[i]:
                    q.append(i)

#---------------------------------------------------------------
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]      # 그래프 생성
visited1 = [False] * (N + 1)             # 방문 여부를 저장하는 리스트
visited2 = [False] * (N + 1)  

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)               # 무방향 그래프라면 양방향으로 추가

# 각 노드의 인접 리스트를 오름차순으로 정렬
for i in range(1, N + 1):
    graph[i].sort()

dfs(graph, V, visited1)  # DFS 시작
print()
bfs(graph, V, visited2)  # BFS 시작
