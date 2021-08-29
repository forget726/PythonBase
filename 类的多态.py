class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print(f"{self.name}在快快乐乐的在玩耍")
class Keji(Dog):
    def game(self):
        print(f"{self.name}是一只柯基犬，"
              f"开心愉快的玩耍！")
class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self):
        print(f"{self.name}和{dog.name}一起开心的玩耍")

dog = Keji("旺旺")
xiaoming=Person("明哥哥")
dog.game()
xiaoming.game_with_dog()