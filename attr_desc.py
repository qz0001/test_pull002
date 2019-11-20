from datetime import date,datetime
class InField:
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass
class User:
    age=InField()
    def __init__(self,name,birthday):
        self.name=name
        self.birthday=birthday
        self._age=0
    # def get_age(self):
    #     return  datetime.now().year-self.birthday.year
    # @property #把函数变成属性描述符
    # def age(self):
    #     return datetime.now().year - self.birthday.year
    # @age.setter
    # def age(self,value):
    #     self._age=value
if __name__ == '__main__':
    user=User("bady",date(year=1987,month=1,day=1))
    user.age=35
    print("我是王辉")
