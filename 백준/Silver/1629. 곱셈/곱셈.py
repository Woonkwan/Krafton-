def dac(a, b, c):
    if b == 1:
        return a % c  # b가 1일 때 a를 c로 나눈 나머지 반환

    if b % 2 == 0:
        return (dac(a, b // 2, c) ** 2) % c  
		# b가 짝수일 때, dac(a, b // 2, c)를 제곱한 값에 c로 나눈 나머지 반환
    
    else:
        return ((dac(a, b // 2, c) ** 2) * a) % c  
		# b가 홀수일 때, dac(a, b // 2, c)를 제곱한 값에 a를 곱하고 c로 나눈 나머지 반환

a, b, c = map(int, input().split())  # 입력으로 a, b, c 값을 받음
print(dac(a, b, c))  # dac 함수에 a, b, c 값을 전달하여 결과 출력