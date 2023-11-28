import turtle

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = turtle.Screen()
        self.screen.title("Ping Pong game")
        self.screen.bgcolor("white")
        self.screen.setup(width=width, height=height)

    def listen(self, left_pad, right_pad):
        self.screen.listen()
        self.screen.onkeypress(left_pad.paddle_up, "a")
        self.screen.onkeypress(left_pad.paddle_down, "z")
        self.screen.onkeypress(right_pad.paddle_up, "Up")
        self.screen.onkeypress(right_pad.paddle_down, "Down")
    
    def refresh(self):
        self.screen.update()