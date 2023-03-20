import pytest

from classes.Point import Point


def test_point_creation():
    point = Point(3)
    assert point.point == 3


def test_point_increase():
    point = Point(5)
    point.increase()
    assert point.point == 6


def test_point_increase_multiple():
    point = Point(10)
    point.increase()
    point.increase()
    point.increase()
    point.increase()
    point.increase()
    assert point.point == 15

if __name__ == "__main__":
    pytest.main()