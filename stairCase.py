from turtle import *

speed('slow')
distance(100)
sides = 10
for i in range(sides):
    fd(20)
    rt(90)
    fd(20)
    lt(90)
    hideturtle()
mainloop()