import turtle

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.end_fill()
#hey
def draw_serbian_flag():
    x = -200
    y = 100
    width = 400
    height = 200
    draw_rectangle(x, y, width, height/2, '#0C4076')
    draw_rectangle(x, y-height/2, width, height/2, '#D7141A')

turtle.speed(0)
draw_serbian_flag()
turtle.done()
