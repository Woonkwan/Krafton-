import sys
from collections import deque

N, M = map(int, input().split())
indegree = [0 for i in range(N+1)]
graph = [[] for i in range(N+1)]




for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] = indegree[b] + 1
        
# -------------------여기까지가 그래프와 진입차수를 만든거        
def topology_sort():
        result = [] #결과로 순서를 나열
        q = deque()

        for i in range(1, N + 1):
            if indegree[i] == 0:
                 q.append(i)   #이게 고민이었는데 왜 그냥 인덱스 번호를 넣냐
                               #그냥 그게 노드 번호임.
# ---------------------시작임. 먼저 시작할 노드 번호를 q에 셋팅임.
        while q:  #q에 아무것도 없을 때까지!
             now = q.popleft()
             result.append(now) #q의 맨왼쪽을 빼면서 순서를 나열
             for j in graph[now]:
                  indegree[j] = indegree[j] - 1 #진입차수를 1씩 뺌

                  if indegree[j] == 0:
                       q.append(j)
        for i in result:
                  print(i, end = ' ')
topology_sort()