#!/usr/bin/env python3
from typing import Dict


L = ['Bart', 'Lisa', 'Adam']
n=0

while n<=len(L)-1:        #while方法实现
    print("hellow,"+L[n])
    n=n+1

for name in L:            #for方法实现
    print("hello,"+name)


n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


s = set([1, 2, 3])
s = dict([1, 2, 3])