pass  # 解法1
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i * 100 + j * 10 + k, end=' ')
print()
pass  # 解法2
from itertools import permutations

nums = [1, 2, 3, 4]
it = permutations(nums, 3)
seq = list(it)
result = [sum([row[i] * 10 ** (2 - i) for i in range(3)]) for row in seq]
print(f'一共有{len(result)}个三位数。')
for i, j in enumerate(result, 1):
    print(f'第{i:2d}个：{j}')
