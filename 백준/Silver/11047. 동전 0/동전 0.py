n, m = map(int, input().split())

numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

numbers.sort(reverse=True)

cnt = 0

for i in numbers:
    cnt += m // i  # 여기를 수정함
    m = m % i  # 여기를 수정함

print(cnt)
