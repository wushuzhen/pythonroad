a = 10
print("a:",a)
def test01(m):
    print("m:",id(m))
    m = 20
    print(m)
    print("m:",id(m))

print(a)
test01(a)

def test02(a,b,c,d):
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))

test02(10,20,30,40)
test02(d=20, b=40, a=10, c=100)

def test03(a, b, c=10, d=15):
    print("{0}-{1}-{2}-{3}".format(a,b,c,d))

test03(2,3)
test03(2,3,4)

g = [lambda a:a*2, lambda b:b*3 ]
print(g[0](6))

h = [test02,test03]
print(h[0](3,4,5,6))


s = "print('abcde')"
eval(s)

a = 10
b = 20
c = eval("a+b")
print(c)

dictl = dict(a=100,b=200)

d = eval("a+b",dictl)
print(d)