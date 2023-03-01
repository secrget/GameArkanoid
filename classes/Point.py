import pygame

class Point:
    """
    Class representing a score in the game.

    Attributes:
        score: The current score of the game.
    """
    def __init__(self, point: int):
        """
        The constructor for the Score class.

        Parameters:
            score: The starting score for the game.
        """
        self.point = point

    def increase(self):
        """
        Increases the score by 1.
        """
        self.point += 1