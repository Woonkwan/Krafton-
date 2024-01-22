import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())    #V =  정점,  E = 간선
visited = [False] * (V + 1)         #[False, False, False, False, False, False] 같이 방문을 표시하기 위해 만들어 줌.
graph = [[] for _ in range(V + 1)]  #[[],[],[].....[]]의 빈 인접 리스트를 만들어 줌.
q = [(0, 1)]                        #0= 가중치, 1=시작노드
for _ in range(E):                  #간선수 만큼 반복
    A, B, C = map(int, input().split()) #A=정점, B=정점, C=가중치
    graph[A].append((C, B))             #(가중치, 정점)
    graph[B].append((C, A))             #(가중치, 정점)

cnt = 0
ans = 0
while q:                                #q에 요소가 있는 동안.
    if cnt == V:                        #: 모든 정점을 방문했으면 반복을 중단
        break
    cost, now = heapq.heappop(q)        #우선순위 큐에서 가장 가중치가 낮은 간선을 추출
    if not visited[now]:                #추출된 간선의 정점을 [now]가 아직 방문하지 않았으면
        visited[now] = True             #방문 처리
        ans += cost                     #가중치를 더함.
        cnt += 1
        for next in graph[now]:         #현재 정점에 인접한 간선들을 우선순위 큐에 추가
            heapq.heappush(q, (next[0], next[1]))   #next[0]을 기준으로 낮은 것을 넣음.
print(ans)