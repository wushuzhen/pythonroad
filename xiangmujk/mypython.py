a = 10
print("a:",a)
def test01(m):
    print("m:",id(m))
    m = 20
    print(m)
    print("m:",id(m))

print(a)
test01(a)