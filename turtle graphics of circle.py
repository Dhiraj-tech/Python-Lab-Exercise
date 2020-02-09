import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
pen.speed(0)
for i in range(50):
    pen.circle(5*i)
    pen.circle(-5*i)
    pen.left(i)
turtle.done()
