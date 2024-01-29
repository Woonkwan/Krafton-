N = int(input().strip())
sudle = []

for _ in range(N):
    su = tuple(map(int, input().split()))
    sudle.append(su)

sudle.sort(key=lambda x: (x[1], x[0]))

last_end_time = 0
count = 0
for start, end in sudle:
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)
