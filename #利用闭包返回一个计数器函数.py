#利用闭包返回一个计数器函数
#每次调用它返回递增整数
def createCounter():
    ax=0
    def counter():
        #引用父级变量不能改变指向,所以用nolocal函数
        nonlocal ax  
        ax=ax+1
        return ax
    return counter
#测试
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

#方法二：利用len()记录计数状态 秀啊！ 
#只要是外部函数调用内部函数的变量 比如lst列表变量
def createCounter():
    lst = []

    def counter():
        lst.append(0)
        return len(lst)
    return counter
#方法三：利用生成器
def createCounter():
    def g():    #生成器生成有序数列1，2，3......
        n=0
        while 1:
            n+=1
            yield n
    a=g()
    def counter():
        return next(a)  #每次调用next()函数获得生成器的下一个返回值
    return counter
#方法四：利用可变数据类型list
def createCounter():
    L=[0]   #初始化列表L为0
    def counter():
        L[0]+=1     #L[0]指的是列表L的第一个元素，为一个可变变量
        return L[0]
    return counter