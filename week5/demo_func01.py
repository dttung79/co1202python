import turtle as t

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

def move_forward(size):
    t.penup()
    t.forward(size)
    t.pendown()

## main program
size = 150
draw_square(size)
for i in range(2):
    move_forward(2 * size)
    draw_square(size)

t.exitonclick()
