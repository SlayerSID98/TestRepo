import turtle
t=turtle.Turtle()
t.speed(50)
turtle.bgcolor("black")
for i in range(240):
    t.color("cyan")
    t.circle(i)
    t.left(20)

turtle.done()
