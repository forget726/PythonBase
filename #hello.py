str="hello world!"
str1=int(input ("请输入数字，并按Enter键确认:"))   #获取输入值
if str1==1:     #判断变量输入
    print (str1)
elif str1 <=5:
    print ("您输入的数字不是1，但是小于5")
else:
    print ("您输入的数字大于5，输出字符:\n"+str)