import ball
import paddle
import screen

pp_ball = ball.Ball()
left_pad = paddle.Paddle(-400, 0)
right_pad = paddle.Paddle(400, 0)
sc = screen.Screen(1000, 600)
sc.listen(left_pad, right_pad)

while True:
    sc.refresh()
    pp_ball.start()
    pp_ball.check_border_collision(sc.width, sc.height)
    pp_ball.check_paddle_collision(left_pad, right_pad)