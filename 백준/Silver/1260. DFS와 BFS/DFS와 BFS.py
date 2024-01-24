from collections import deque
#========================================
def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end = " ")
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)
#========================================
def bfs(graph, v, visited_bfs):

    q = deque([v])

    while q:    
        A = q.popleft()
        if not visited_bfs[A]:
            visited_bfs[A] = True
            print(A, end = " ")
            for i in graph[A]:
                if not visited_bfs[i]:
                    q.append(i)



#========================================입출력 및 그래프 생성, 정렬 부문
N, M ,V = map(int, input().split())
graph = [[] for i in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for i in range(M):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort()

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)