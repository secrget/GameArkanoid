import pytest

from classes.Brick import Brick
from classes.Ball import Ball


def test_brick_creation():
    brick = Brick([0, 0], 50, 20)
    assert brick.position == [0, 0]
    assert brick.width == 50
    assert brick.height == 20
    assert brick.status == "unharmed"

#new file
def test_brick_destroy():
    brick = Brick([0, 0], 50, 20)
    brick.destroy()
    assert brick.status == "destroyed"


def test_brick_collision():
    brick = Brick([0, 0], 50, 20)
    ball = Ball([0, 0], [5, 5])
    assert brick.check_collision(ball) == True


if __name__ == "__main__":
    pytest.main()
