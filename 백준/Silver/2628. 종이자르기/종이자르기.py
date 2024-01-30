import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

N = int(input())

sudle_1 = [0]
sudle_2 = [0]

for _ in range(N):
    su_a, su_b = map(int, input().split())
    if su_a == 0:
        sudle_1.append(su_b)
    else:
        sudle_2.append(su_b)
sudle_1.append(Y)
sudle_2.append(X)
sudle_1.sort()
sudle_2.sort()

max_paper = 0
for i in range(1, len(sudle_1)):
    for j in range(1, len(sudle_2)):
        paper = (sudle_1[i] - sudle_1[i - 1]) * (sudle_2[j] - sudle_2[j - 1])
        max_paper = max(max_paper, paper)

print(max_paper)
