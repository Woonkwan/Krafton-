import sys

def dfs(graph, start, visited):
    visited[start] = True
    connected_nodes.append(start)
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

input = sys.stdin.readline
V = int(input())  # V = 정점
E = int(input())  # E = 간선
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

connected_nodes = []  # 1번 노드와 연결된 노드를 저장할 리스트
visited = [False] * (V + 1)  # 방문 여부를 체크하는 리스트

# 1번 노드부터 탐색 시작
dfs(graph, 1, visited)

# 결과 출력
print(len(connected_nodes)-1)
