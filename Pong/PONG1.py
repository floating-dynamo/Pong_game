import turtle
import winsound

# The main screen
tu = turtle.Screen()
tu.bgcolor("black")
tu.setup(width=800, height=600)
tu.title("Pong by @floatingDynamo")
tu.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard  Binding
tu.listen()
tu.onkeypress(paddle_a_up, "w")
tu.onkeypress(paddle_a_down, "s")
tu.onkeypress(paddle_b_up, "Up")
tu.onkeypress(paddle_b_down, "Down")

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Scoring
point_a = 0
point_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.sety(260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# Game loop
while True:
    tu.update()
    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        point_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(point_a, point_b),
                  align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        point_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(point_a, point_b),
                  align="center", font=("Courier", 24, "normal"))

    # Paddles and Ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
