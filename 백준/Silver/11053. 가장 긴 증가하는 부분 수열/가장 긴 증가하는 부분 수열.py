N = int(input().strip())
sudle = list(map(int, input().split()))

# 각 위치에서 끝나는 가장 긴 증가하는 부분 수열의 길이를 저장하는 리스트
lengths = [1] * N

# 모든 요소에 대해 반복
for i in range(N):
    # 현재 요소보다 앞에 있는 요소들에 대해 반복
    for j in range(i):
        if sudle[j] < sudle[i]:
            lengths[i] = max(lengths[i], lengths[j] + 1)

# 가장 긴 증가하는 부분 수열의 길이 출력
print(max(lengths))