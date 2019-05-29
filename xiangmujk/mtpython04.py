def test01(n):
    print("test01:",n)
    if n==0 :
        print("over")
    else:
        test01(n-1)
    print("test01***",n)

def test02():
    print("test02")

test01(2)

# 使用递归函数计算阶层

def fa(n):
    if n==1:
        return 1
    else:
        return n*fa(n-1)

result = fa(5)
print(result)

# 测试嵌套函数的定义

def outer():
    print("outer running")

    def inner():
        print("inner running")
    
    inner()

outer()

# 测试nonlocal global 关键字的用法

def outer01():
    b = 10
    def inner01():
        nonlocal b
        print("inner01:",b)
        b = 20

    inner01()
    print("outer b:", b)

outer01()

# 测试LEGB
str = "global str"
def outer02():
    str = "outer"
    def inner02():
        str = "inner"
        print(str)
    inner02()
outer02()