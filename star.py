from turtle import *

speed('slow')

sides = 5
distance = 100
for i in range(sides):
    
    fd(distance)
    rt(360/sides)

hideturtle()
mainloop()