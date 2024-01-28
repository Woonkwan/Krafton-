import sys

def ans(N):
    if N == 0: return 1
    if N == 1: return 1

    a, b = 1, 1
    for i in range(2, N + 1):
        a, b = b, (a + b) % 15746

    return b


N = int(input().strip())
print(ans(N))
