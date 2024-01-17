import sys

KEY = sys.stdin.readline().strip().split()
M = int(KEY[0])
N = int(KEY[1])

li = []
result = []

for i in range(1, M+1):
    li.append(i)

count = 1

while len(li) != 0:
    temp = li[0]
    li.pop(0)

    if count % N == 0:
        result.append(temp)
    else:
        li.append(temp)
    count = count + 1 

result_str = ", ".join(map(str, result))  # 리스트의 각 요소를 문자열로 변환하고 쉼표로 구분
print("<" + result_str + ">")
