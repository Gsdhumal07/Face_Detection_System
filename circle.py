import turtle as TK

t = turtle.Turtle()

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

while(1):
    for i in range(6):
        for colour in ['red','black','green','blue','yellow','white']:
            turtle.color(colour)
            turtle.circle(100)
            turtle.left(10)

turtle.hideturtle()
turtle.mainloop()
