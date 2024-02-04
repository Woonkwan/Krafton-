import sys
input = sys.stdin.readline
numbers = []
number = input().split()
numbers.append(number)
# x,y , w, h
x = int(numbers[0][2]) - int(numbers[0][0])
y = int(numbers[0][3]) - int(numbers[0][1])
a = min(int(numbers[0][0]), x)
b = min(int(numbers[0][1]), y)
c = min(a, b)

print(c)