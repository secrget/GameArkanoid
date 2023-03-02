import pygame

class Point:
    """
    Class representing a point in the game.

    Attributes:
        point: The current score of the game.
    """
    def __init__(self, point: int):
        """
        Parameters:
            point: The starting score for the game.
        """
        self.point = point

    def increase(self):
        """
        Plus point by 1.
        """
        self.point += 1