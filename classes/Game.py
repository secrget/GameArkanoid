import pygame as pg
from classes.Ball import Ball
from classes.Paddle import Paddle
from classes.Brick import Brick
from classes.Point import Point
#from  elase.BrickArray import bricks

class Game:
    """The Game class represents the Breakout game.

        Attributes:
            screen: Поверхня екрана для відображення гри.
            clock:  для керування частотою кадрів гри
            ball: Об'єкт м'яч
            paddle: об'єкт ракетка .
            bricks: Список блокових об'єктів
            point: Бали

        Methods:
            run: Основний цикл гри. Він виконує такі дії як оновлення та рендер, доки гра не закінчиться.
            update_game: Оновлює стан об’єктів гри.
            render_game: Рендерить ігрові об’єкти на екрані.
            check_game_over: Цей метод перевіряє, чи закінчилась гра
             """

    def __init__(self, screen_size: list[int,int]):
        """Конструктор для класу Game.."""

        pg.init()
        self.screen = pg.display.set_mode(screen_size)
        self.clock = pg.time.Clock()
        self.ball = Ball([450, 400], [3, 3])
        self.paddle = Paddle([450, 450], 80, 20)
        self.bricks = [Brick([j, i], 50, 20) for i in range(50, 200, 30) for j in range(50, 700, 70)]
        self.point = Point(0)


    def run(self):
        """Основний цикл гри. Він виконує такі дії як оновлення та рендер, доки гра не закінчиться."""
        launched = True
        while launched:   # запуск безкінечного циклу поки launched не змінится на False або не буде вказано break
            for event in pg.event.get():  # Цикл збирає всі події
                if event.type == pg.QUIT:   # Якщо подія натискання на хрестик гра закінчуєтся
                    launched = False
            keys = pg.key.get_pressed()   # отримуємо всі події на клавіатурі
            if keys[pg.K_LEFT]:
                self.paddle.move(-8)
            elif keys[pg.K_RIGHT]:
                self.paddle.move(8)
            elif keys[pg.K_ESCAPE]:  # якщо клавіша з кодом K_ESCAPE була натиснута, то виходимо з циклу
                break
                # Це просто опис            self.update_game()  # оновлюємо стан гри.
            self.render_game()   # відображаємо стан гри.
            if self.check_game_over():  # Перевірка на закінчення гри
                break
            self.clock.tick(100)  # Обмежуємо кіликість кадрів для гри
        pg.quit()  # закриваємо pygame

    def update_game(self):
        """Updates the state of the game objects."""
        self.ball.move()  # Починаємо рух м'яча
        if self.ball.position[0] <= 0: # Перевіряє чи м'я відбився від лівоїчастини екрану
            self.ball.speed[0] = -self.ball.speed[0]  # Змінюємо напрям м'яча по вісі Х на протележний
        elif  self.ball.position[0] >= self.screen.get_width():  # Перевіряє чи м'я відбився від  правої частини екрану
            self.ball.speed[0] = -self.ball.speed[0]
        elif self.ball.position[1] <= 0:  # Перевіряє чи м'я відбився від верхньої частини екрану
            self.ball.speed[1] = -self.ball.speed[1]   # Змінюємо напрям м'яча по вісі Y на протележний
        elif self.paddle.check_collision(self.ball):  # Перевіряємо, чи м'яч зіткнувся з ракеткою.
            self.ball.speed[1] = -self.ball.speed[1]  # Змінюємо напрям м'яча по вісі Y на протележний
        for block in self.bricks:  # Проходимося по всіх блоках
            if block.check_collision(self.ball):  # Перевірка чи м'яч зіткнувся з блоком
                block.destroy()     # руйнуємо блок
                self.ball.speed[1] = -self.ball.speed[1]   # Змінюємо напрям м'яча по вісі Y на протележний
                self.point.increase()   # додаєм бал до поінт


    def render_game(self):

        """Renders the game objects on the screen."""
        self.screen.fill((0, 0, 0))  # малюємо  чорний екран
        pg.draw.circle(self.screen, (255, 4, 25), self.ball.position, 20)  # Малюємо коло
        pg.draw.rect(self.screen, (25, 255, 26), (self.paddle.position[0], self.paddle.position[1], self.paddle.width, self.paddle.height))   # Малюємо квадрат
        for block in self.bricks: # Цикл для проходу по всім елемантам масиву
            if block.status == "unharmed": # перевіряємо чи блок неушкоджений  bricks
                pg.draw.rect(self.screen, (255, 255, 255),(block.position[0], block.position[1], block.width, block.height))  # Малюємо блок
        type = pg.font.Font(None, 25) # Задаємо шрифт 25 пікселів в даожину
        point_text = type.render("Point: {}".format(self.point.point), True, (255, 2, 255))  # Малюємо текст на екрані
        self.screen.blit(point_text, [0, 0]) # Розміщюємо його в лівому верхньому вуглі
        pg.display.update()  #  оновлює вікно з грою, щоб відобразити зміни.


    def check_game_over(self):
        """ This method checks if the game is over."""
        if self.ball.position[1] > self.screen.get_height():  # Перевірка чи м'яч по осі Y опустився  нижче ніжнього краю вікна
            return True
        # Проходимо через кожен блок
        for block in self.bricks:
            # Якщо блок не пошкоджений, збільшуємо лічильник на 1
            if block.status == "unharmed":
                return False
        # Якщо лічильник дорівнює 0, то повертаємо True (гра закінчена)
        return True
