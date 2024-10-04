
import turtle as trtl
wn = trtl.Screen()
wn.setup(width=800,height=800)
painter = trtl.Turtle()

radius = 50 #size of circle
circles = 5

width=800 #total width of the screen how far the circles will reach
distance = (width - (2*radius))/(circles-1) #calculation for how far the circles are apart, equidistant

for i in range (circles):
    x = -350 + i * distance #because the circle radius is 50 we need to subtract the border lenght by 50 for the starting positon so the edge touches.
    painter.penup()
    painter.goto(x,0)
    painter.pendown()
    painter.circle(radius)

wn.mainloop()