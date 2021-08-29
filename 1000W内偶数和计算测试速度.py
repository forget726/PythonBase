import time

# t1 = time.time()
# print(sum([e for e in range(1, 10000000) if not e % 2]))
# t2 = time.time()
# t = t2 - t1
# print(t)
#
#
# #FT大佬优化代码
#
# s = time.time()
# print(sum(range(0 , 10000000, 2)))
# print(time.time()-s)

#FT优化代码 2.0，等差数列求和

s1 = time.time_ns()
print (((10000000-2)//2)*(10000000-2+2)//2)
print(time.time_ns()-s1)