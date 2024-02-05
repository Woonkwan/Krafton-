import sys
input = sys.stdin.readline

x = int(input())
a = x % 4
b = x % 400
c = x % 100

def yoon():
    if a == 0 and b == 0:
        return 1
    elif a == 0 and c != 0:
        return 1
    else:
        return 0

print(yoon())