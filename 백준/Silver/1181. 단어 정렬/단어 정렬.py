N = int(input())
word_list = []

for _ in range(N):
    word = input()
    word_list.append(word)

word_list = list(set(word_list))
word_list.sort()
word_list.sort(key = len)

for i in word_list:
    print(i)