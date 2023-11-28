import turtle

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(40)
        self.ball.shape("circle")
        self.ball.color("blue")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 5
        self.ball.dy = -5

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def check_border_collision(self, screen_width, screen_height):
        if self.ball.ycor() > (screen_height / 2):
            self.ball.sety((screen_height / 2))
            self.ball.dy *= -1
    
        if self.ball.ycor() < -(screen_height / 2):
            self.ball.sety(-(screen_height / 2))
            self.ball.dy *= -1
    
        if self.ball.xcor() > (screen_width / 2):
            self.ball.goto(0, 0)
            self.ball.dy *= -1
        
        if self.ball.xcor() < -(screen_width / 2):
            self.ball.goto(0, 0)
            self.ball.dy *= -1

    def check_paddle_collision(self, left_pad, right_pad):
        if (self.ball.xcor() > 360 and self.ball.xcor() < 370) and (self.ball.ycor() < right_pad.ycor() + 40 and self.ball.ycor() > right_pad.ycor() - 40):
            self.ball.setx(360)
            self.ball.dx*=-1
        
        if (self.ball.xcor()<-360 and self.ball.xcor()>-370) and (self.ball.ycor()<left_pad.ycor() + 40 and self.ball.ycor() > left_pad.ycor() - 40):
            self.ball.setx(-360)
            self.ball.dx*=-1
