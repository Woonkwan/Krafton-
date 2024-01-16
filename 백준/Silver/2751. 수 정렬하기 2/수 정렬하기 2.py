import sys  # sys 모듈 임포트

N = int(input())
Num_List = [0] * N

for i in range(N):
    Num_List[i] = int(sys.stdin.readline().strip()) 

Num_List.sort()
for n in Num_List:
    print(n)