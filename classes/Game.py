import pygame as pg
from classes.Ball import Ball
from classes.Paddle import Paddle
from classes.Brick import Brick
from classes.Point import Point
#from  elase.BrickArray import bricks

class Game:
    """The Game class represents the Breakout game.

        Attributes:
            screen: The screen surface to display the game.
            clock: The clock to control the game's framerate.
            ball: The ball object in the game.
            paddle: The paddle object in the game.
            bricks: A list of block objects in the game.
            score: The score object in the game.

        Methods:
            run: The main loop of the game. It updates and renders the game until the game is over.
            update: Updates the state of the game objects.
            render: Renders the game objects on the screen.
            check_game_over: This method checks if the game is over by checking if the ball has fallen out of the screen or if all bricks have been destroyed.
     """

    def __init__(self, screen_size: list[int,int]):
        """The constructor for the Game class.

            Parameters:
                screen_size: The size of the screen to display the game.
        """
        pg.init()
        self.screen = pg.display.set_mode(screen_size)
        self.clock = pg.time.Clock()
        self.ball = Ball([450, 400], [3, 3])
        self.paddle = Paddle([450, 450], 80, 20)
        self.bricks = [Brick([j, i], 50, 20) for i in range(50, 200, 30) for j in range(50, 700, 70)]
        self.point = Point(0)


    def run(self):
        """The main loop of the game. It updates and renders the game until the game is over."""
        launched = True
        while launched:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    launched = False
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.paddle.move(-8)
            elif keys[pg.K_RIGHT]:
                self.paddle.move(8)
            elif keys[pg.K_ESCAPE]:
                break   # launched = False
            self.update()
            self.render()
            if self.check_game_over():
                break
            self.clock.tick(60)
        pg.quit()

    def update(self):
        """Updates the state of the game objects."""
        self.ball.move()
        if self.ball.position[0] <= 0 or self.ball.position[0] >= self.screen.get_width():
            self.ball.speed[0] = -self.ball.speed[0]
        elif self.ball.position[1] <= 0:
            self.ball.speed[1] = -self.ball.speed[1]
        elif self.paddle.check_collision(self.ball):
            self.ball.speed[1] = -self.ball.speed[1]
        for block in self.bricks:
            if block.check_collision(self.ball):
                block.destroy()
                self.ball.speed[1] = -self.ball.speed[1]
                self.point.increase()


    def render(self):

        """Renders the game objects on the screen."""
        self.screen.fill((0, 0, 0))
        pg.draw.circle(self.screen, (255, 4, 25), self.ball.position, 20)
        pg.draw.rect(self.screen, (25, 255, 26), (self.paddle.position[0], self.paddle.position[1], self.paddle.width, self.paddle.height))
        for block in self.bricks:
            if block.status == "unharmed":
                pg.draw.rect(self.screen, (255, 255, 255),(block.position[0], block.position[1], block.width, block.height))
        type = pg.font.Font(None, 25)
        point_text = type.render("Point: {}".format(self.point.point), True, (255, 2, 255))
        self.screen.blit(point_text, [0, 0])
        pg.display.update()


    def check_game_over(self):
        """
            This method checks if the game is over by checking if the ball has fallen out of the screen or if all bricks have been destroyed.

            Returns:
                bool: True if the game is over, False otherwise.
        """
        if self.ball.position[1] > self.screen.get_height():
            return True
        elif len([block for block in self.bricks if block.status == "unharmed"]) == 0:
            return True
        return False
