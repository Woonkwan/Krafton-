from itertools import combinations

height_list = []
for _ in range(9):
    height = int(input())
    height_list.append(height)

height_combinations = list(combinations(height_list, 7))     #7개의 모든 조합
for height_combination in height_combinations:
    if sum(height_combination) == 100:
        height_combination = sorted(list(height_combination))
        for h in height_combination:
            print(h)
        break