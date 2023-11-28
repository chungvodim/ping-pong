import turtle

class Paddle:
    def __init__(self, xpos, ypos):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("black")
        self.paddle.shapesize(stretch_wid=6, stretch_len=2)
        self.paddle.penup()
        self.paddle.goto(xpos, ypos)

    def paddle_up(self):
        self.paddle.sety(self.paddle.ycor() + 20)
 
 
    def paddle_down(self):
        self.paddle.sety(self.paddle.ycor() - 20)

    def ycor(self):
        return self.paddle.ycor()
    
    def set_ycor(self, ypos):
        return self.paddle.sety(self.paddle.ycor() + ypos)
    
    def xcor(self):
        return self.paddle.xcor()
    
    def set_xcor(self, xpos):
        return self.paddle.sety(self.paddle.ycor() + xpos)
