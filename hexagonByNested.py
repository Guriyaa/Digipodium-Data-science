from turtle import *

speed('slow')
distance = 100
sides = 6
for i in range(sides):
    fd(distance)
    rt(360/sides)
    for i in range(sides):
        fd(distance/2)
        rt(360/sides)
        write(i)
        mainloop()