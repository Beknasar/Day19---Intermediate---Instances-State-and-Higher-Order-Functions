from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def clear():
    tim.home()
    tim.clear()


# turtle_moves = {
#     'w': move_forwards,
#     "s": move_backwards,
#     "a": counter_clockwise,
#     "d": clockwise,
#     "c": tim.clear,
# }
screen.listen()
# for key, fun in turtle_moves.items():
#     screen.onkey(key=key, fun=fun)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
