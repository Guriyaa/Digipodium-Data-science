from turtle import *

speed('slow')
sides = 10
distance = 100
for i in range(10):
  fd(distance)
  rt(360/sides)

  hideturtle()
mainloop()