import pygame as py
import colorama as co
from components import Ball, Paddle

py.init()
co.init()

WIDTH = 800
HEIGHT = 700
FPS = 60
BALL_RADIUS = 7

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (19, 58, 38)


PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("PONG--GAME")

white = co.Fore.WHITE
yellow = co.Fore.YELLOW
red = co.Fore.RED
blue = co.Fore.BLUE
green = co.Fore.GREEN



def handle_movement_paddle(keys, left_paddle, right_paddle) -> None:
    if keys[py.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[py.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[py.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[py.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def draw(win, paddles, ball) -> None:
    win.fill(GREEN)

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        py.draw.rect(win, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

    ball.draw(win)

    py.display.update()


def main() -> None:
    run = True
    clock = py.time.Clock()

    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT //
                         2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                          2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break

        keys = py.key.get_pressed()
        handle_movement_paddle(keys, left_paddle, right_paddle)
        ball.move()

    py.quit()


if __name__ == '__main__':
    print(yellow + '\t\t Welcome to this pong Game \n\n')

    main()

#######################Created by Userlg ##################################################################
