import turtle
t = turtle.Pen()
my_colors = ("red", "green", "blue", "skyblue", "yellow")
for i in range(5):
    t.penup()
    t.goto(0, -i * 20)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(50+i*20)

for i in range(11):
    t.penup()
    t.goto(0, -20*i)
    t.pendown()
    t.goto(200, -20*i)
for i in range(11):
    t.penup()
    t.goto(200-20*i, -200)
    t.pendown()
    t.goto(200-20*i, 0)
turtle.done()

def getsum(a):
    '''获取a的累加值'''
    sum = 0
    for x in range(a):
        sum += x
    return sum

print(getsum(5))