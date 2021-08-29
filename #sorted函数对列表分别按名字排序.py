#sorted函数对列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
#测试
L2 = sorted(L, key=by_name)
print(L2)


#sorted函数对列表分别按成绩排序
def by_score(t1):
    return t1[-1]
L3 = sorted(L,key=by_score,reverse=False)
print(L3)