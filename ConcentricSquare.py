import turtle as trtl
trtl.Screen().bgcolor("light green")
painter = trtl.Turtle()
painter.speed(15)

#init colors, starting position, incrementation, and first square size
colors_list = ["red", "blue", "green", "purple", "gold"]
x = -125 
y = -125
move = 25
forward = 300

#Draw squares
for i in range(5):
    painter.goto(x,y)
    x = x + move
    y = y + move
    forward = (forward - (move * 2)) #Incrementation
    painter.fillcolor(colors_list[i]) #Iterate thru the colors list, draw each square based on each color from the list
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