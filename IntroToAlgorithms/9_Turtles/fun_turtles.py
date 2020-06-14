import turtle

screen = turtle.Screen()
diego = turtle.Turtle()  # create a turtle object
diego.shape("turtle")

# how to draw a square?
diego.fillcolor("yellow")
diego.begin_fill()
diego.color("yellow")
for _ in range(4):
    diego.forward(100)
    diego.left(90)
diego.end_fill()

# how to draw a triangle?
diego.fillcolor("green")
diego.begin_fill()
diego.color("green")
for _ in range(3):
    diego.forward(100)
    diego.left(120)
diego.end_fill()

# how to draw a rectangle? (with:100, height:50)
diego.fillcolor("blue")
diego.begin_fill()
diego.color("blue")
for _ in range(2):
    diego.forward(100)
    diego.left(90)
    diego.forward(50)
    diego.left(90)
diego.end_fill()

screen.exitonclick()