import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
#=============================
def dfs(start):
    #print(start,end=', ')
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            visited[i]=True
    
#=============================

N, M = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visited=[False]*(N+1)
count=0
for i in range(1,N+1):
    if visited[i]==False:
        dfs(i)
        count+=1

print(count)



