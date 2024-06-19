rom collections import defaultdict

words = defaultdict(list)
words_range = list(map(int, input().split()))
loop_length = sum(words_range)
for i in range(loop_length):
    current_word = input()
    if i < words_range[0]:
        words['group_a'].append(current_word)
    else:
        indexes = [i+1 for i in range(len(words['group_a'])) if words['group_a'][i] == current_word]
        if indexes:
            print(*indexes)
        else:
            print(-1)
