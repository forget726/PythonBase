#求和

lst = ['A', 'A', 'A', 'B', 'B', 'C', 'B','D','C']
seq, string = [''] + lst + [''], ''
index = [i for i in range(len(seq) - 1) if seq[i] != seq[i + 1]]
for i in range(len(index) - 1):
    counter = index[i + 1] - index[i]
    string += f'{lst[index[i]]}{counter}'
print(string)


#FT大佬的方法

import re

lst = ['A', 'A', 'A', 'B', 'B', 'C', 'B']
mat = re.finditer(r'(.)\1*', ''.join(lst))
for node in mat:
    string = node.group()
    print(f'{string[0]}{len(string)}', end='')