import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for i in range(1, N+1):
    if i < 100:
        cnt += 1
    else:
        j = str(i)
        if int(j[0]) - int(j[1]) == int(j[1]) - int(j[2]):
            cnt += 1
print(cnt)