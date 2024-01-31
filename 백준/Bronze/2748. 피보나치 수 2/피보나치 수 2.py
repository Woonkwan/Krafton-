import sys
input = sys.stdin.readline

def fibo(N):
    if N <= 0:
        return 0
    elif N == 1:
        return 1
    else:
        a, b = 0 ,1
        for _ in range(N-1):
            b , a = a +b , b
        return b
        
N = int(input())
print(fibo(N))