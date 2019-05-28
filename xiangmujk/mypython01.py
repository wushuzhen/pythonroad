print("hello, pycharm")
a = input("请输入一个小于10的数字：")
if int(a) < 10:
    print(a)

b = []
if b:
    print("空的列表是false")

c = True
if c:
    print("c")

s = input("请输入一个数字：")

if int(s)<10:
    print("s是小于10的数字")
else:
    print("s是大于等于10的数字")

print("s是小于10的数字" if int(s)<10 else "s是大于等于10的数字")

score = int(input("请输入一个分数"))
if score>100 or score < 0:
    print("请输入一个0到100的数字")
else:
    if score > 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("E")

num = 0
sun = 0
while num <= 10:
    sun += num
    num += 1

print(sun)

sum_all = 0
sum_add = 0
sum_even = 0
for x in range(100):
    sum_all += x
    if x%2 == 1:
        sum_add += x
    else:
        sum_even += x
print(sum_all,sum_add,sum_even)


