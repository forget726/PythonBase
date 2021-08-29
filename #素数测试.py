import time

# sum=0
# for i in range(2,2001):
#     n = False #默认不是素数，如果是素数，跳出循环
#     for j in range(2,i):
#         if i%j == 0:
#             n = True
#             break
#     if n == False:
#         sum+=1
#         print(i,end=',')
# print('\n素数个数为%s'%sum)

pass  # 1W内所有质数,简化版
# s = time.time()
# l = []
# for i in range(2, 100000000):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         pass
#         # print(i, end=" ")
#         # l.append(i)
# # print(l)
# print(time.time()-s)

pass  # 筛选法选出1000W内质数
# def primes(n):
#     P = []
#     f = []
#     for i in range(n + 1):
#         if i > 2 and i % 2 == 0:
#             f.append(1)
#         else:
#             f.append(0)
#     i = 3
#     while i * i <= n:
#         if f[i] == 0:
#             j = i * i
#             while j <= n:
#                 f[j] = 1
#                 j += i + i
#         i += 2
#     P.append(2)
#     for i in range(3, n, 2):
#         if f[i] == 0:
#             P.append(i)
#
#     return P
# if __name__ == '__main__':
#     start = time.time()
#     n = 100000000
#     p = primes(n)
#     end = time.time()
#
#     print(p)
#     print(f'耗时{end - start:.2f}s')

pass  # 分解质因数
# l = []
# n = int(input("你输入你要分解的质因数："))
# n2 = n
# while True:
#     for i in range(2, 90):
#         if n % i == 0:
#             l.append(i)
#             n //=i
#             break
#     else:
#         break
# if len(l) != 1:
#     print(l)
# else:
#     print(f"{n2}是质数！")
pass  # 计算一亿以内所有质数，代码小于10行，用时小于10秒
import numpy as np

s = time.time()
n = 100000000
# np.set_printoptions(threshold=np.inf)
prime = np.arange(n)
# print(prime)
# exit()
prime[4::2] = 0
prime[1] = 0
for i in range(3, int(n ** 0.5) + 1, 2):
    if prime[i] != 0:
        prime[i * i::i] = 0
print(prime[prime > 0])
e = time.time()
print(e-s)