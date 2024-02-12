import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

left = 1  # 최소한의 날짜
right = V  # 최대 가능한 날짜

while left <= right:
    mid = (left + right) // 2  # 이분 탐색을 위한 중간 값 계산
    height = A * mid - B * (mid - 1)  # 중간 날짜에서의 높이 계산
    
    if height >= V:  # 목표 높이에 도달한 경우
        answer = mid  # 결과 저장
        right = mid - 1  # 더 작은 범위에서 확인
    else:
        left = mid + 1  # 더 큰 범위에서 확인

print(answer)  # 결과 출력