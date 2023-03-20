import pytest
from classes.Paddle import Paddle
from classes.Ball import Ball

def test_paddle_move():
    paddle = Paddle([0, 0], 10, 20)
    paddle.move(5)
    assert paddle.position == [5, 0]

def test_paddle_collision():
    paddle = Paddle([0, 0], 10, 20)
    ball = Ball([5, 15], 1)
    assert paddle.check_collision(ball) == True

if __name__ == "__main__":
    pytest.main()