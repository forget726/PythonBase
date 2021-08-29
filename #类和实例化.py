#；类和实例化
class Student(object):
    def __init__(self, name, gender,age):
        self.__name = name
        self.__gender = gender
        self.__age=age
    def get_gender(self):
        return self.__gender
    def get_age(self):
        return self.__age
    def set_gender(self):
        if self.__gender=='男'or'女' or '保密':
            return self.__gender
        else:
            raise ValueError('性别输入有误！')
    def set_age(self,gender):
        if self.__age>=0:
            self.__age=gender
        else:
            raise TypeError
bart = Student('Bart Simpson', '男',59)
print(bart.get_gender())
bart.set_age(99)
print(bart.get_age())
