import turtle

box = turtle.Turtle()

for i in range(100):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)

    turtle.forward(i * 5)
