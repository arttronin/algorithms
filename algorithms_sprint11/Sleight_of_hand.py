# ID 82706556

import collections

k = int(input())
matrix = [list(
    map(int, "".join(c for c in input() if c.isalnum()))) for i in range(4)]
count_matrix = []


def append_matrix_list(matrix):
    for i in range(4):
        count_matrix.extend(matrix[i])
    return count_matrix


def score(dict_count, k):
    score = 0
    hands = int(k*2)
    for key, value in dict_count.items():
        if hands >= value:
            score += 1
    print(score)


append_matrix_list(matrix)
dict_count = dict(collections.Counter(count_matrix))
score(dict_count, k)
