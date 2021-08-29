import turtle
p = turtle.Pen()
turtle.bgcolor("black")
sides = 7
colors = ["red","orange","yellow","green","cyan","blue","purple"]
for x in range(360):
    p.pencolor(colors[x%sides])
    p.forward(x*3/sides+x)
    p.left(360/sides+1)
    p.width(x*sides/200)
done()