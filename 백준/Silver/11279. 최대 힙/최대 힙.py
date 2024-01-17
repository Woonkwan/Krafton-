import sys
import heapq

input = sys.stdin.readline

N = int(input())
H = []  # 메인 (힙으로 사용)
C = []  # 출력

for _ in range(N):
    num = int(input())

    if num != 0: 
        heapq.heappush(H, -num)  # 최대 힙을 위해 음수로 변환하여 추가
    else:
        if H:
            max_value = -heapq.heappop(H)  # 최대값 추출
            C.append(max_value)
        else:
            C.append(0)

output = "\n".join(map(str, C))
print(output)
