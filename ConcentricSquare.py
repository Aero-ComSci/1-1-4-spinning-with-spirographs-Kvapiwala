import turtle as trtl
trtl.screensize(800, 800, "light green")
painter = trtl.Turtle()
painter.speed(15)

#list for the colors of each square
colors_list = ["red", "blue", "green", "purple", "orange"]

x = 0 
y = 0
move = 25
forward = 300

#Draw squares
for i in range(5):
    x = x + move
    y = y + move
    forward = (forward - (move * 2))
    painter.fillcolor(colors_list[i])
    painter.begin_fill()
    for i in range(4):
        painter.forward(forward)
        painter.left(90)
    painter.end_fill()
    painter.penup()
    painter.goto(x,y)
    painter.pendown()


wn = trtl.Screen()
wn.mainloop()

