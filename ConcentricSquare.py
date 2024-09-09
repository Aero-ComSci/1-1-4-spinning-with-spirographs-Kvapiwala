import turtle as trtl
trtl.screensize(800, 800, "light green")
painter = trtl.Turtle()
painter.speed(0)

#Dictionary for the colors of each square
colors = {
    "colors": ["red", "blue", "yellow", "green", "purple"]
}

x = 0 
y = 0
move = 25
forward = 50

#Draw squares
while(x <= 0 , y <= 0):
    for i in range(5):
        for i in range(4):
            x = x - move
            y = y - move
            forward = (forward + (move * 2))
            painter.forward(forward)
            painter.left(90)
            painter.penup()
            painter.goto(x,y)
            painter.pendown()



wn = trtl.Screen()
wn.mainloop()

