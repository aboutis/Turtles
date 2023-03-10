from turtle import Turtle, Screen

timmy = Turtle()


def foward():
    timmy.forward(10)


def backward():
    timmy.backward(10)


def left():
    timmy.left(10)


def right():
    timmy.right(10)


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=foward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=left)
screen.onkey(key="a", fun=right)
screen.exitonclick()
