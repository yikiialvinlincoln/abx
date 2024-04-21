import turtle

# Function to draw a blue circle
def draw_blue():
    tr.color("blue")
    tr.penup()
    tr.goto(-110, -25)
    tr.pendown()
    tr.circle(45)

# Function to draw a black circle
def draw_black():
    tr.color("black")
    tr.penup()
    tr.goto(0, -25)
    tr.pendown()
    tr.circle(45)

# Function to draw a red circle
def draw_red():
    tr.color("red")
    tr.penup()
    tr.goto(110, -25)
    tr.pendown()
    tr.circle(45)

# Function to draw a yellow circle
def draw_yellow():
    tr.color("yellow")
    tr.penup()
    tr.goto(-55, -75)
    tr.pendown()
    tr.circle(45)

# Function to draw a green circle
def draw_green():
    tr.color("green")
    tr.penup()
    tr.goto(55, -75)
    tr.pendown()
    tr.circle(45)

# Function to draw all colors
def draw_all_colors():
    draw_blue()
    draw_black()
    draw_red()
    draw_yellow()
    draw_green()

# Set up the screen and turtle
screen = turtle.Screen()
screen.title("Olympic Rings")
tr = turtle.Turtle()
tr.pensize(5)

# Draw all colors
draw_all_colors()

# Hide the turtle and display the result
tr.hideturtle()
screen.mainloop()
