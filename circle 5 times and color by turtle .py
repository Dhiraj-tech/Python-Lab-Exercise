import turtle
pen=turtle.Turtle()
pen.fillcolor("red")
pen.begin_fill()
for i in range(5):
    pen.circle(50*i)
    pen.up()
    pen.sety((50*i)*(-1))
    pen.down()
pen.end_fill()
turtle.done()
