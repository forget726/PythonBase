#csv生成函数
def c_csv():
    with open('s.csv','w') as f:
        f.write('姓名\t学号\t班级\t性别\n')
        f.write('曹尼玛\t1\t1\t女\n')
        f.write('史珍香\t1\t1\t女\n')
        f.write('毕云涛\t1\t1\t男\n')
        f.write('李时珍\t1\t1\t男\n')

if __name__=='__main__':
    c_csv()
    with open('s.csv','r') as f1:
        print(f1.read())
    print('csv生成完毕')
c_csv()