import sys

n = int(sys.stdin.readline())

a = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))


for num in b:
    if num in a:
        print(1)
    else:
        print(0)