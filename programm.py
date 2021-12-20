import turtle


turtle.setup(700, 700)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Карта прохода по помещению")

# instantiate (create) tess and set her attributes
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

# instantiate alex
alex = turtle.Turtle()

# draw an equilateral triangle with tess
tess.forward(320)
tess.left(120)
tess.forward(320)
tess.left(120)
tess.forward(320)
tess.left(120)

# turn tess around and move her away from the origin
tess.right(180)
tess.forward(320)

# make alex draw a square
alex.forward(200)
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(200)

wn.exitonclick()
