import turtle

window = turtle.Screen()
window.bgcolor("pink")
window.title("Feliz")

pen = turtle.Turtle()
pen.color ("red")
pen.fillcolor("red")
pen.pensize(3)
pen.speed(7)
pen.begin_fill()
pen.left(140)
pen.forward(224)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
    pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(224)
    pen.end_fill()
    pen.up()
    pen.goto(0, -70)
    pen.down()
    pen.color("black")
    pen.write("Para voce ")

    pen.hideturtle()

    turtle.done()