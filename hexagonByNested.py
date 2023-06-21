from turtle import *

speed('slow')
distance = 100
sides = 6
for i in range(sides):
    pencolor('indigo')
    fd(distance)
    rt(360/sides)
    for i in range(sides):
      pencolor('green')
      fd(distance/3)
      rt(360/sides)
write(i)
hideturtle()
mainloop()