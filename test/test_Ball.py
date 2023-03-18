import pytest

from classes.Ball import Ball


def test_init():
    ball = Ball([0, 0], [1, 1])
    assert ball.position == [0, 0]
    assert ball.speed == [1, 1]

def test_move():
    ball = Ball([0, 0], [1, 1])
    ball.move()
    assert ball.position == [1, 1]

def test_move_multiple_times():
    ball = Ball([0, 0], [1, 1])
    ball.move()
    ball.move()
    assert ball.position == [2, 2]


if __name__ == "__main__":
    pytest.main()