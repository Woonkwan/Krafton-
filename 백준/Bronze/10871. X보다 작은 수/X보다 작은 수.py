import sys
input = sys.stdin.readline

N, X = map(int, input().split())
numbers = list(map(int, input().split()))

ans = []
for i in range(len(numbers)):
    if numbers[i] < X:
        ans.append(numbers[i])

print(" ".join(map(str, ans)))