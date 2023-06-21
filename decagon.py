from turtle import *

speed('slow')
sides = 6 
distance = 100
for i in range(6):
  fd(distance)
  rt(360/sides)

  hideturtle()
mainloop()