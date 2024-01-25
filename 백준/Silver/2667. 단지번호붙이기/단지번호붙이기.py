import sys
from collections import deque

n = int(sys.stdin.readline())
array = []

# 지도 정보 입력 받기
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().strip())))

# 방문 여부를 확인하는 배열
visited = [[False] * n for _ in range(n)]

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1  # 현재 단지에 속한 집의 수

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count

# 각 단지별 집의 수를 저장할 리스트
house_counts = []

# 모든 위치에 대하여 집이 있는 경우 BFS 수행
for i in range(n):
    for j in range(n):
        if array[i][j] == 1 and not visited[i][j]:
            house_counts.append(bfs(i, j))

# 출력
house_counts.sort()
print(len(house_counts))  # 총 단지수 출력
for count in house_counts:
    print(count)  # 각 단지 내 집의 수 출력