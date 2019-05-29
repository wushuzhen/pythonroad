class Student:     #首字母大写 多个单词采用驼峰原则
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def say_score(self):        #self 必须位于第一个参数
        print("{0}的分数是：{1}".format(self.name,self.score))

sl = Student("gaoqi",18)  #使用类名（）调用构造函数
sl.say_score()


Student("wsx",98).say_score()