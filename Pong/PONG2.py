import turtle
import winsound
# Main Screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.hideturtle()
pen.penup()
pen.sety(250)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
tm = turtle.Turtle()
tm.speed(0)
tm.color("white")
tm.hideturtle()
tm.penup()
tm.setx(340)
tm.sety(280)
tm.write("Sridhar™", align="center", font=("Courier", 12, "normal"))
tu = turtle.Screen()
tu.title("Sridhar's Pong Game")
tu.bgcolor("black")
tu.setup(width=800, height=600)
tu.tracer(0)
Score = 0

# Paddle
Paddle = turtle.Turtle()
Paddle.speed(0)
Paddle.color("red")
Paddle.shape("square")
Paddle.shapesize(stretch_wid=1, stretch_len=8)
Paddle.penup()
Paddle.goto(0, -280)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.color("yellow")
Ball.shape("circle")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.09
Ball.dy = 0.09

# Functions


def Paddle_left():
    x = Paddle.xcor()
    x -= 20
    Paddle.setx(x)


def Paddle_right():
    x = Paddle.xcor()
    x += 20
    Paddle.setx(x)


tu.listen()
tu.onkeypress(Paddle_left, "Left")
tu.onkeypress(Paddle_right, "Right")
# Main game loop
while True:
    tu.update()
    # Ball Movement
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)
    # Border Checking
    if(Ball.ycor() > 290):
        Ball.sety(290)
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        Ball.dy *= -1

    if(Ball.xcor() > 390):
        Ball.setx(390)
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        Ball.dx *= -1

    if(Ball.xcor() < -390):
        Ball.setx(-390)
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        Ball.dx *= -1

    if(Ball.ycor() < -290):
        winsound.PlaySound("button-3.wav", winsound.SND_ASYNC)
        Ball.goto(0, 0)
        Ball.dy *= -1
        pen.clear()
        Score = 0
        pen.write("Score: {}".format(Score), align="center",
                  font=("Courier", 24, "normal"))
    # Ball - Paddle Collision
    if Ball.ycor() < -270 and Ball.ycor() > -280 and Ball.xcor() < Paddle.xcor() + 80 and Ball.xcor() > Paddle.xcor() - 80:
        Ball.sety(-270)
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
        Ball.dy *= -1
        Score += 1
        pen.clear()
        pen.write("Score: {}".format(Score), align="center",
                  font=("Courier", 24, "normal"))
