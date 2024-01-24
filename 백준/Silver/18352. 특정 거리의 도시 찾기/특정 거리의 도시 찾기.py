import sys
from collections import deque
input=sys.stdin.readline  # 대화형 환경에서는 주석 처리

def bfs(graph, X, K):
    q = deque([(X, 0)])
    chk = [False] * len(graph)
    chk[X] = True  # 출발 도시에 대한 초기 방문 체크
    ans = []

    while q:
        A, depth = q.popleft()
        if depth == K:
            ans.append(A)
        for i in graph[A]:
            if not chk[i]:
                chk[i] = True
                q.append((i, depth + 1))
    
    return -1 if len(ans) == 0 else sorted(ans)  # 결과를 오름차순으로 정렬

# 입력 받기
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

# 출력
result = bfs(graph, X, K)

if result == -1:
    print(-1)
else:
    for node in result:
        print(node)
