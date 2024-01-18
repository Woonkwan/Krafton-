import sys
from itertools import combinations

cnt, pluss = map(int, input().split())  # 예: 5 0
A = list(map(int, input().split()))     # 예: -7 -3 -2 5 8

count = 0                               #카운트를 올리는 방식으로
for i in range(1, cnt + 1):             
    for com in combinations(A, i):     #(A,1)부터 노가다 ㄱㄱ
        if sum(com) == pluss:
                count += 1

print(count)