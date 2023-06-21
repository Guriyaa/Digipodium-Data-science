from turtle import *

speed('slow')

sides = 5
distance = 100
for i in range(sides):
    pencolor('red')
    rt(144)
    fd(distance)
    pencolor('green')
    lt(72)
    fd(distance)
    dot(10)
hideturtle()
mainloop()