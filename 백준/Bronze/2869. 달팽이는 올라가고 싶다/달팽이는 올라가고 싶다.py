import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

days = (V - B) / (A - B)  # 도착지까지 날짜 계산
print(int(days) if days == int(days) else int(days) + 1)  # 정수로 변환하여 출력
