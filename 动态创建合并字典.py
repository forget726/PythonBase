ll = [
    {"name": "sun", "hobby": "滑雪"},
    {"name": "sun", "hobby": "吃饭"},
    {"name": "sun", "hobby": "游泳"},
    {"name": "amy", "hobby": "抽烟"},
    {"name": "amy", "hobby": "烫头"},
    {"name": "min", "hobby": "喝酒"},
]

# FT大佬代码
# l = {}
# for i in ll:
#     if i["name"] in l:
#         l[i["name"]].append(i["hobby"])
#     else:
#         l[i["name"]] = [i["hobby"]]
# print(l)

# l = {}
# for j in ll:
#     # 动态创建字典名字命名作为变量的空列表
#     exec(f"{j['name']} = []")
# for i in ll:
#     # 把名字的值添加到对应的列表
#     eval(i["name"]).append(i["hobby"])
#     #生成字典
#     l[i["name"]] = eval(i["name"])
# print(l)
pass  # 动态创建变量 并且通过枚举赋值
# l = [1, 2, True, 12.58, '你好', [1, 2, 3], {'name': "小明"}, (12, 3)]
# for i, j in enumerate(l):
#     exec(f"{'str' + str(i)} = j")
# print(str1, str2, str3, str4, str5, str6, str7)

# mylist = [1,2,3,4,5,6,7,8,9]
# for a, b in enumerate(mylist):
#     locals()['a' + str(a)] = b
# print(a0,a1,a2,a3,a4,a5,a7,a8)

pass  # locals方法创建
# names = locals()
# for i in range(5):
#     names['str' + str(i)] = i
# str0 = "abc"
# str1 = [1, 2, 3]
# print(str0, str1, str2, str3,)
