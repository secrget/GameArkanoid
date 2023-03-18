import pygame

class Brick:
    """
    A class representing a Block in a Breakout game.

    Attributes:
        position: A 2-element list representing the position of the Block on the game screen.
        width:  The width of the Block.
        height: The height of the Block.
        status: The status of the Block, either "unharmed" or "destroyed".

    Methods:
        check_collision(ball): Checks if the ball has collided with the Block.
        destroy(): Changes the status of the Block to "destroyed".
    """
    def __init__(self, position: list[int, int], width: int, height: int):
        self.position = position
        self.width = width
        self.height = height
        self.status = "unharmed"

    def check_collision(self, ball):
        """
        Checks if the ball has collided with the Block.

        Parameters:
            ball : The Ball object that the collision is being checked against.

        Returns:
            bool: True if the ball has collided with the Block, False otherwise.
        """
        if self.status == "unharmed" and\
                ( self.position[0] <= ball.position[0] <= self.position[0] + self.width) and\
                (self.position[1] <= ball.position[1] <= self.position[1] + self.height):
            return True
        return False

    def destroy(self):
        """
        Changes the status of the Block to "destroyed".
        """
        self.status = "destroyed"