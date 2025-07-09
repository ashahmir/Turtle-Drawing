from turtle import Turtle, Screen

ben = Turtle()
screen = Screen()
penWidth = 1
print("Press 0-9 to Change Pen Color")
print("Use '+' and '-' to change Pen Thickness")
def forwards():
    ben.forward(10)

def backwards():
    ben.forward(-10)

def turn_right():
    ben.right(10)

def turn_left():
    ben.right(-10)

def clear_screen():
    screen.reset()
def red():
    ben.color("red")

def blue():
    ben.color("blue")

def green():
    ben.color("green")

def yellow():
    ben.color("yellow")

def orange():
    ben.color("orange")

def purple():
    ben.color("purple")

def pink():
    ben.color("pink")

def black():
    ben.color("black")

def brown():
    ben.color("brown")

def cyan():
    ben.color("cyan")

def bolder():
    global penWidth
    penWidth += 1
    ben.pensize(penWidth)

def lighter():
    global penWidth
    if penWidth > 1:
        penWidth -= 1
    ben.pensize(penWidth)


screen.listen()
screen.onkeypress(key="w", fun=forwards)
screen.onkeypress(key="s", fun=backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear_screen)
screen.onkeypress(key="+", fun=bolder)
screen.onkeypress(key="-", fun=lighter)
screen.onkeypress(key="0", fun=red)
screen.onkeypress(key="1", fun=blue)
screen.onkeypress(key="2", fun=green)
screen.onkeypress(key="3", fun=yellow)
screen.onkeypress(key="4", fun=orange)
screen.onkeypress(key="5", fun=purple)
screen.onkeypress(key="6", fun=pink)
screen.onkeypress(key="7", fun=black)
screen.onkeypress(key="8", fun=brown)
screen.onkeypress(key="9", fun=cyan)

screen.exitonclick()
