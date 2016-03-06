# Open turtle module
import turtle
wn = turtle.Screen()
# Set window size
wn.setup (width=900, height=900, startx=0, starty=0)
# Set background to light blue 
wn.bgcolor("lightblue")
# Show every 2 points as it draws and set speed of drawing to speed it up process
turtle.tracer(2,1)

# Creating turtle named snowman
snowman = turtle.Turtle()

# Set the outline color to black at size 2 and filling color to white
snowman.color("black")
snowman.fillcolor("white")
snowman.pensize(2)
snowman.shape("blank")

# Move bottom of snowman to proper spot
snowman.up()
snowman.goto(0,-150)
snowman.down()

# Bottom circle creation and fill circle with white
snowman.begin_fill()
for i in range(360):
    snowman.forward(2)
    snowman.left(1)
snowman.end_fill()

# Move middle part of snowman to proper spot
snowman.up()
snowman.goto(0,0)
snowman.down()

# Middle circle creation and fill circle with white
snowman.begin_fill()
for i in range(360):
    snowman.forward(1.5)
    snowman.left(1)
snowman.end_fill()

# Move top part of snowman to proper spot
snowman.up()
snowman.goto(0,150)
snowman.down()

# Top circle creation and fill circle with white
snowman.begin_fill()
for i in range(360):
    snowman.forward(1)
    snowman.left(1) 
snowman.end_fill()

# Eye creation and make pensize larger
snowman.pensize(5)
snowman.up()
snowman.goto(30,220)
snowman.dot()

snowman.up()
snowman.goto(-30,220)
snowman.dot()

# Set nose color
snowman.color("orange")
snowman.fillcolor("orange")

# Nose Location
snowman.up()
snowman.goto(0,200)
snowman.down()

# Nose Shape and fill color
snowman.begin_fill()
snowman.forward(30)
snowman.right(165)
snowman.forward(30)
snowman.right(90)
snowman.forward(7)
snowman.end_fill()

# Buttons, enlarging button size and making them black
snowman.pensize(7)
snowman.color("black")
snowman.up()
snowman.goto(0,80)
snowman.dot()
snowman.up()
snowman.goto(0,100)
snowman.dot()
snowman.up()
snowman.goto(0,120)
snowman.dot()
snowman.up()
snowman.goto(0,140)
snowman.dot()

# Hat shape drawing, change pensize, and filled in
snowman.pensize(2)
snowman.color("black")
snowman.fillcolor("gray")
snowman.begin_fill()
snowman.up()
snowman.goto(-70,230)
snowman.down()
snowman.right(90)
snowman.forward(120)
snowman.left(90)
snowman.forward(20)
snowman.left(90)
snowman.forward(25)
snowman.right(90)
snowman.forward(70)
snowman.left(90)
snowman.forward(70)
snowman.left(90)
snowman.forward(70)
snowman.right(90)
snowman.forward(25)
snowman.left(90)
snowman.forward(20)
snowman.end_fill()

# Right Arm drawing,change pensize, and arm color
snowman.pensize(5)
snowman.color("chocolate4")
snowman.up()
snowman.goto(-70,100)
snowman.down()
snowman.right(160)
snowman.forward(120)
snowman.right(20)
snowman.forward(20)
snowman.right(180)
snowman.forward(20)
snowman.right(80)
snowman.forward(20)

# Left Arm drawing
snowman.up()
snowman.goto(70,100)
snowman.down()
snowman.right(160)
snowman.forward(120)
snowman.right(20)
snowman.forward(20)
snowman.right(180)
snowman.forward(20)
snowman.right(80)
snowman.forward(20)

# Ends program on click
wn.exitonclick()
    
