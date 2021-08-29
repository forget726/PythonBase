import re

pass  # 推理题
# a = [{'乙':2},{'丙':1}]
# b = [{'丙':2},{'丁':3}]
# c = [{'甲':2},{'丁':4}]
# result = []
# for i in a:
#     for j in b:
#         for k in c:
#             dt = {}
#             dt.update(i)
#             dt.update(j)
#             dt.update(k)
#             print(dt,end='\t')
#             if len(dt) == 3:
#                 result.append([(key,value) for key,value in dt.items()])
# print()
# print(result)
# for n in result:
#     if n[0][1] != n[1][1] and n[0][1] != n[2][1] and n[2][1] != n[1][1]:
#         print(n)
pass  # 输出带多个引号的字典值
# l = [
#     {'Yu': ["Smoking""Drinking Beer""Cigarettes"], 'Guo': [' crosstalk', 'drama']},
#     ]
# print(l[0]["Yu"])
pass  # 正则匹配*+不同
a = "我是中文ljsadfladlfk"

print(re.findall(r"[\u4e00-\u9fa5]*", a))
pass  # yeild问题
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(2)
#     print('step 3')
#     yield(3)
# o_0 = odd()
# for x in range(3):
#     print('in odd()' + str( next(odd())) )
# for x in range(3):
#     print('in o_0' + str( next(o_0) ) )
