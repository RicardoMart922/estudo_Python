import turtle

t = turtle.Turtle()

screen = turtle.Screen()

screen.bgcolor('black')

t.pensize(2)
t.speed(0)

while(True):
    for i in range(6):
        for colors in ['red', 'blue', 'magenta', 'green', 'yellow', 'white']:
            t.color(colors)
            t.circle(100)
            t.left(10)

t.hideturtle