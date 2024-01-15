N = int(input())

def hano(x, y, z, N):
    if N == 0:
        return

    hano(x, z, y, N - 1)
    print(x,z)
    hano(y, x, z, N - 1)

print((1 << N) - 1)
if N <= 20:
    hano(1, 2, 3, N)