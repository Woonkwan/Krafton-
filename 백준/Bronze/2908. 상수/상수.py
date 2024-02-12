import sys
input = sys.stdin.readline

A, B = input().split()

a1 = A[0]
a2 = A[2]
a = a2 + A[1] + a1 

b1 = B[0]
b2 = B[2]
b = b2 + B[1] + b1

x= max(int(a),int(b))
print(x)