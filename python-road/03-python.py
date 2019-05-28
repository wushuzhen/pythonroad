import turtle
import math
# 定义多点位的坐标

x1,y1 = 100,100
x2,y2 = 100,-100
x3,y3 = -100,-100
x4,y4 = -100,100

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

turtle.write(distance)
turtle.goto(x2,y2)

distance = math.sqrt((x2-x3)**2 + (y2-y3)**2)

turtle.write(distance)


turtle.goto(x3,y3)

distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

turtle.write(distance)

turtle.goto(x4,y4)

distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

turtle.write(distance)
