from turtle import*
speed('fastest')
size = 10
angle = 45
colors = ['red','purple','green','pink','orange','yellow']
while True:
    pencolor(colors[size%5])
    fd(size)
    lt(angle)
    size += 1