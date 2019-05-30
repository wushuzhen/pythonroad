# 析构方法
# class Person:
#     def __del__(self):
#         print("销毁对象{0}".format(self))
# p1 = Person()
# p2 = Person()

# del p2
# print("cheng'y'xu")


# class Person:
#     def say_hai(self):
#         print("hello")

#     def say_hai(self, name):
#         print("hello:", name)

# class Person:
#     def work(self):
#         print("努力上班 ！")

# def play_ganme(s):
#     print("{0}在玩游戏".format(s))

# Person.play = play_ganme
# p = Person()
# p.work()
# p.play()

#测试私有属性

# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def __work(self):
#         print("好好工作，赚钱娶媳妇！")
#         print("年龄：{0}".format(self.__age))

# e = Employee("搞起", 18)
# print(e.name)

# print(e._Employee__age)
# print(dir(e))
# e._Employee__work()

#测试@property的用法

# class Employee:
#     @property
#     def salary(self):
#         print("salary run...")
#         return 10000

# empl = Employee()
# print(empl.salary)

#用法

class wsz:
    def __init__(self,name ,salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("录入错误！")

    # def get_salary(self):
    #     return self.__salary
    # def set_salary(self, salary)
    #     if 1000<salary<50000:
    #         self.__salary = salary
    #     else:
    #         print("录入错误！")

empl = wsz("wushuzhen", 30000)
# print(empl.salary)
# empl.salary = -20000
# print(empl.salary)

print(empl.salary)
empl.salary(-20000)
print(empl.salary)