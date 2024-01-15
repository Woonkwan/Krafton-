numbers = []

for i in range(9):
    add = int(input())
    numbers.append(add)

print(max(numbers))
print(numbers.index(max(numbers))+1)