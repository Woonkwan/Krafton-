N = int(input())
numbers = []

for i in range(N):
    num = int(input())
    numbers.append(num)

numbers.sort()

for i in range(N):
    print(numbers[i], end = '\n')