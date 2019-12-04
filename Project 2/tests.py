"""import turtle 

star = turtle.Turtle()

for i in range(50):
    star.forward(50)
    star.right(144)
    
turtle.done()"""
"""import turtle 

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()
"""
import turtle
#####screen.delay(5)
screen = turtle.Screen()

# click the image icon in the top right of the code window to see
# which images are available in this trinket
image = "g.gif"

# add the shape first then set the turtle shape
screen.addshape(image)
turtle.shape(image)

screen.bgcolor("lightblue")

move_speed = 10
turn_speed = 10

# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
