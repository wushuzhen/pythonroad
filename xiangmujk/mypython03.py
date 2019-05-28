# import math
# import time
# def test01():
#     start = time.time()
#     for i in range(10000000):
#         math.sqrt(30)
#     end = time.time()
#     print("耗时{0}".format((end - start)))

# def test02():
#     start = time.time()
#     b = math.sqrt
#     for i in range(10000000):
#         b(30)
#     end = time.time()
#     print("耗时{0}".format((end - start)))

# test01()
# test02()


# a = [10, 20]
# print(id(a))
# print(a)
# print("########")
# def test01(m):
#     print(id(m))
#     m.append(300)
#     print(id(m))

# test01(a)
# print(a)


import copy
def testCopy():
    '''测试浅拷贝'''
    a = [10,20,[5,6]]
    b = copy.copy(a)
    print("a:",a)
    print("b:",a)
    b.append(30)
    b[2].append(7)
    print("浅拷贝....")
    print("a:",a)
    print("a:",b)

def testdeepCopy():
    '''测试深拷贝'''
    a = [10,20,[5,6]]
    b = copy.deepcopy(a)
    print("a:",a)
    print("b:",a)
    b.append(30)
    b[2].append(7)
    print("深拷贝....")
    print("a:",a)
    print("a:",b)