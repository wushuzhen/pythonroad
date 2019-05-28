r1 = {"name":"18","age":18,"salary":10000,"city":"北京"}
r2 = {"name":"18","age":18,"salary":10000,"city":"北京"}
r3 = {"name":"18","age":18,"salary":10000,"city":"北京"}

tb = [r1,r2,r3]

sa = tb[1].get("salary")
print(sa)


for i in range(len(tb)):
    print(tb[i].get("salary"))

for i in range(len(tb)):
    print(tb[i].get("salary"),tb[i].get("age"),tb[i].get("salary"),tb[i].get("city"))
