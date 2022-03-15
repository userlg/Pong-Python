import pygame as py

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (19, 58, 38)

class Ball:
    COLOR = WHITE
    MAX_VEL = 5

    def __init__(self, x, y, radius) -> None:
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win) -> None:
        py.draw.circle(win, self.COLOR,  (self.x, self.y), self.radius)

    def move(self) -> None:
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self) -> None:
        self.x =self.original_x
        self.y =self.original_y
        self.y_vel = 0
        self.x_vel *= 1


class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height) -> None:
        self.x = self.original_x =x
        self.y = self.original_y =y
        self.width = width
        self.height = height

    def draw(self, win) -> None:
        py.draw.rect(win, self.COLOR,
                     (self.x, self.y, self.width, self.height))

    def move(self, up=True) -> None:
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self) -> None:
        self.x = self.original_x
        self.y = self.original_y
