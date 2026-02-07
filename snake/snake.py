import turtle
import time

delay = 0.1

#Set up the screen
window = turtle.Screen()
window.title("Snake Game Example")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0) #turns off screen updates

#Snake head 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Functions to control the snake
def up():
    head.direction = "up"

def down():
    head.direction = "down"

def left():
    head.direction = "left"

def right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Keyboard bindings
window.listen()
window.onkeypress(up, "w")
window.onkeypress(down, "s")
window.onkeypress(left, "a")
window.onkeypress(right, "d")

#Main game loop
while True:
    window.update() #updates the screen

    move() #move the snake
    time.sleep(delay)

window.mainloop()