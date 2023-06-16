import turtle as t
shape = input('What shape do you want to draw (triangle / square): ')
if shape != 'triangle' and shape != 'square':
    print('Invalid shape')
else:
    if shape == 'triangle':
        for i in range(3):
            t.forward(200)
            t.left(120)
    else:
        for i in range(4):
            t.forward(200)
            t.left(90)
    t.exitonclick()
    print('Done')
