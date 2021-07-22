import turtle
turtle.title("Pong Game")

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)#this speed is for animation of the paddle
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.color("white")
paddle1.penup()
paddle1.goto(-350, 0)

#Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.color("white")
paddle2.penup()
paddle2.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0.20
ball.dy = 0.20

paddle1_score = 0
paddle2_score = 0
#score
score = turtle.Turtle()
score.speed(0)
score.hideturtle()
score.color("white")
score.penup()
score.goto(0,250)
score.write("Left: 0  Right: 0 ", align="center", font=("Courier", 24, "normal"))



#paddle moving
def paddle1_up():
    y = paddle1.ycor()#it gives y cordinate
    y +=20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -=20
    paddle1.sety(y)

def paddle2_up():
    y =paddle2.ycor()
    y +=20
    y =paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

#Calling functions
window.listen()#waiting for the keyboard input
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")



#creating a game loop just like in Unity(update function)
while True:
    window.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 400:
        ball.setx(400)
        ball.goto(0,0)
        ball.dx *= -1
        paddle1_score +=1
        score.clear()
        score.write("Left: {}  Right: {} ".format(paddle1_score, paddle2_score), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -400:
        ball.setx(-400)
        ball.goto(0,0)
        ball.dx *= -1
        paddle2_score +=1
        score.clear()
        score.write("Left: {}  Right: {} ".format(paddle1_score, paddle2_score), align="center",
                    font=("Courier", 24, "normal"))

    #touching paddles
    if ball.xcor() < -340 and ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50:
        ball.dx *= -1



