N = input()


def calculate_min_value(expression):
    # '-'를 기준으로 수식을 분할
    parts = expression.split('-')

    # 첫 번째 부분을 계산
    total = sum(map(int, parts[0].split('+')))

    # 나머지 부분을 계산하여 전체에서 뺀다
    for part in parts[1:]:
        total -= sum(map(int, part.split('+')))

    return total

# 예제 입력 및 출력
print(calculate_min_value(N))