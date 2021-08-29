pass  # 循环遍历字典并且删除指定元素
dic = {"a": 1, "b": 3, "c": 1}
# 把字典的键新建个列表遍历键列表，删除对应值
for i in list(dic.keys()):
    if dic[i] == 1:
        del dic[i]
print(dic)
pass  # 循环遍历列表并且动态删除指定元素
l = [1, 5, 6, 7, 9, 5, 1, 1]
for j in l[:]:
    if j == 1:
        l.remove(j)
print(l)