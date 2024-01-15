N = int(input())

def fac(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * fac(N - 1)


print(fac(N)) 