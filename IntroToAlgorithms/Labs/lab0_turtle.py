import turtle
screen = turtle.Screen()
screen.bgcolor("#90ee90")
screen.screensize(20, 20)
tu = turtle.Turtle()  # create a turtle object
tu.shape("turtle")
tu.color("blue")
tu.stamp()  # Stamp a copy of the turtle shape onto the canvas at the current turtle position.
for _ in range(12):  # repeat 12 times
    tu.penup()  # Pull the pen up – no drawing when moving.
    tu.forward(100)  # Move forward without drawing.
    tu.pendown()  # Pull the pen down – drawing when moving.
    tu.forward(20)  # Move forward with drawing.
    tu.penup()
    tu.forward(20)
    tu.stamp()
    tu.goto(0.00, 0.00)  # Return to the original position.
    tu.left(30)  # turn to left 30 degree.
screen.exitonclick()
