# Import module
import turtle
import winsound

win = turtle.Screen()
win.title("Pong by Kaone")
win.bgcolor("black")
win.setup(width=800, height=600)

win.tracer(0)



# Add 1st Paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-360, 0)

# Add 2nd Paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(360, 0)

# Add Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

# Game scores
pen = turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player 1 = 0, Player 2 = 0", align="center", font=("Courier", 14, "bold"))

#Generate scores
score1 = 0
score2 = 0

# Function to move the paddles:
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y2 = paddle_a.ycor()
    y2 -= 20
    paddle_a.sety(y2)

def paddle_b_up():
    y3 = paddle_b.ycor()
    y3 += 20
    paddle_b.sety(y3)

def paddle_b_down():
    y4 = paddle_b.ycor()
    y4 -= 20
    paddle_b.sety(y4)


# Set Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


#Loop through the game
while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Conditions for when the ball hits the border
    #if ball.xcor
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player 1 = %s, Player 2 = %s" % (score1, score2), align="center", font=("Courier", 14, "bold"))
        winsound.PlaySound("ding.wav", winsound.SND_ASYNC)
        

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player 1 = %s, Player 2 = %s" % (score1, score2), align="center", font=("Courier", 14, "bold"))
        winsound.PlaySound("ding.wav", winsound.SND_ASYNC)


    # To make the ball bounce on the paddle
    if (ball.xcor() > 350 and ball.xcor() < 355) and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55):
        ball.setx(350)
        ball.dx *= -1
        winsound.PlaySound("swoosh.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -350 and ball.xcor() > -355) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-350)
        ball.dx *= -1
        winsound.PlaySound("swoosh.wav", winsound.SND_ASYNC)

# Improving the Game
#Include sound effect -- sound.wave
#Include Pause option in game