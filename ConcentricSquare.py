
import turtle as trtl
trtl.Screen().bgcolor("light green")
painter = trtl.Turtle()
painter.speed(15)

#init colors, starting position, incrementation, and first square size
colors_list = ["light blue", "maroon", "orchid", "dark green", "gold","light blue", "maroon", "orchid", "dark green", "gold","light blue", "maroon", "orchid", "dark green", "gold"]
x = -375 
y = -375
move = 25
forward = 800
painter.pensize(10)

#Draw 5 squares
for i in range(15):
    painter.goto(x,y)
    x = x + move
    y = y + move
    forward = (forward - (move * 2)) #Incrementation
    painter.pencolor(colors_list[i]) #Iterate thru the colors list, draw each square based on each color from the list
    painter.begin_fill()
    for i in range(4):
        painter.forward(forward)
        painter.left(90)
    painter.end_fill()
    painter.penup()
    painter.goto(x,y)
    painter.pendown()
painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()

